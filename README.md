# 🤖 ChattyBot – AI Chatbot Backend

ChattyBot is a full-stack AI chatbot backend built using **FastAPI**, **MongoDB**, and **Ollama (Gemma model)**.  
It supports multi-conversation chat history, conversation-based deletion, and custom AI identity control.

Developed by **Engineer Himanshu**.

---

## 🚀 Features

- ✅ AI responses using Gemma model (via Ollama)
- ✅ Multi-conversation support
- ✅ Chat history per conversation
- ✅ Delete entire conversation
- ✅ MongoDB database integration
- ✅ Custom AI identity (does not expose base model)
- ✅ RESTful API design
- ✅ Ready for frontend integration
- ✅ Deployment-friendly structure (Base URL support)

---

## 🛠 Tech Stack

- **Backend Framework:** FastAPI
- **Database:** MongoDB
- **Database Driver:** Motor (Async MongoDB)
- **AI Model Runtime:** Ollama
- **Model Used:** llama3.2:1b
- **Server:** Uvicorn

---

## 📁 Project Structure

```
project/
│
├── main.py              # Main FastAPI app
├── database.py          # MongoDB connection
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd client
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

If requirements file not created:

```bash
pip install fastapi uvicorn motor requests python-dotenv
```

---

### 4️⃣ Install & Run Ollama

Download Ollama from:
https://ollama.com

Pull the model:

```bash
ollama pull llama3.2:1b
```

Start Ollama server:

```bash
ollama run llama3.2:1b
```

---

### 5️⃣ Start FastAPI Server

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧠 How It Works

### 1️⃣ User sends message to:

```
POST /chat
```

Body:

```json
{
  "message": "Hello",
  "conversation_id": "123456"
}
```

---

### 2️⃣ Backend:

- Sends prompt to Ollama
- Receives AI response
- Saves message + reply in MongoDB
- Returns response to frontend

---

### 3️⃣ Chat History

```
GET /history?conversation_id=123456
```

Returns all messages for that conversation only.

---

### 4️⃣ Delete Conversation

```
DELETE /delete_conversation/{conversation_id}
```

Deletes all messages inside that conversation.

---

## 🗄 Database Structure (MongoDB)

Collection: `chat_collection`

Example document:

```json
{
  "_id": ObjectId,
  "conversation_id": "123456",
  "user_message": "Hello",
  "ai_reply": "Hi there!",
  "timestamp": "2025-02-26T10:00:00"
}
```

---

## 🎯 AI Identity Control

System prompt ensures:

- Bot name: **ChattyBot**
- Created by: **Engineer Himanshu**
- Does NOT mention:
  - Google
  - DeepMind
  - Meta
  - Base model details

---

## 🌐 Frontend Integration

Use a Base URL:

```js
const BASE_URL = "http://127.0.0.1:8000";
```

Example API call:

```js
axios.post(`${BASE_URL}/chat`, {
  message: message,
  conversation_id: currentConversationId
});
```

---

## 🧩 Future Improvements

- User authentication (JWT)
- Streaming responses
- Conversation titles
- Pagination for history
- Deployment on AWS / Render / Railway
- Docker support

---

## 📦 Deployment Ready

When deploying:

- Change BASE_URL
- Use MongoDB Atlas
- Use environment variables for secrets
- Run with production server (Gunicorn)

---

## 👨‍💻 Developer

Engineer Himanshu  
Software Developer  

---

## 📜 License

This project is open-source and free to use.

---

# ⭐ Final Notes

This project demonstrates:

- Backend API design
- AI integration
- Database architecture
- Multi-conversation handling
- Clean separation between frontend & backend

Perfect for portfolio and production-level learning.
