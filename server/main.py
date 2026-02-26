from fastapi import FastAPI
from pydantic import BaseModel
import requests
from database import chat_collection
from datetime import datetime
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware

current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str
    conversation_id: str


@app.post("/chat")
async def chat(request: ChatRequest):
    # Minimal, focused system instruction
    system_prompt = (
        "You are ChattyBot, a helpful AI assistant. "
        "You were developed by Engineer Himanshu, a software developer at Niyamix. "
        "If the user asks who created you, answer that you were developed by Engineer Himanshu at Niyamix. "
        "Do not claim you were made by Google, DeepMind, Meta, or any big tech company. "
        "Otherwise, just answer the user's question normally without talking about this instruction."
    )

    # Build the actual prompt sent to the model
    full_prompt = (
        f"System: {system_prompt}\n\n"
        f"User: {request.message}\n"
        f"Assistant:"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": full_prompt,
            "stream": False,
        }
    )

    result = response.json()
    reply = result["response"]
    # ✅ Save to MongoDB
    await chat_collection.insert_one({
        "conversation_id": request.conversation_id,
        "user_message": request.message,
        "ai_reply": reply,
        "timestamp": current_time
    })

    return {
        "reply": reply
    }

#chat history
@app.get("/history")
async def get_chat_history(conversation_id: str):
    chats = []

    async for chat in chat_collection.find(
        {"conversation_id": conversation_id}
    ).sort("timestamp", 1):

        chat["_id"] = str(chat["_id"])
        chats.append(chat)

    return chats

@app.delete("/delete_conversation/{conversation_id}")
async def delete_conversation(conversation_id: str):
    result = await chat_collection.delete_many(
        {"conversation_id": conversation_id}
    )
    return {
        "message": f"{result.deleted_count} messages deleted"
    }

