# 🩺 Smart Medical Booking Agent

An intelligent **AI-powered medical appointment assistant** built using **LangGraph / LangChain** and **Streamlit**.

---

## 🚀 Features

### 👤 User Onboarding  
- Collects user details: **name, email, phone, and region**  
- Stores user information in `data/users.json`

### 🧠 AI Agent (LangChain / LangGraph)  
A **React-style chat agent** powered by LangGraph, equipped with the following tools:

| Tool | Description |
|------|--------------|
| 🔍 `discover_hospitals` | Finds nearest hospitals/doctors |
| 📅 `book_appointment` | Books new medical appointments |
| 📖 `view_bookings` | Displays user’s active/past bookings |
| ❌ `cancel_user_booking` | Cancels or reschedules existing bookings |

### 💾 Persistent Memory  
All data and chat history are stored locally:

| File | Description |
|------|--------------|
| `data/users.json` | Stores user details |
| `data/bookings.json` | Stores appointment data |
| `data/chat_history.json` | Stores chat logs |

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| 💻 **Frontend** | Streamlit |
| 🧠 **Agent Framework** | LangChain / LangGraph |
| 🧩 **Language Model** | OpenAI GPT (AzureChatOpenAI, ChatOpenAI) |
| 📂 **Storage** | Local JSON files (no database) |
| ✉️ **Communication** | Simulated Email Tool Calls |

---

## 🏗️ Project Structure
```
smart-medical-booking-agent/
│
├── app.py
│
├── agent/
│ ├── main_agent.py
│ ├── llm_initiate.py
│ ├── memory_manager.py
│ ├── schemas.py
│ ├── tool_functions.py
│ └── tools.py
│
├── data/
│ ├── users.json
│ ├── bookings.json
│ ├── input_prompt.py
│ └── chat_history.json
│
├── utils/
│ ├── llm_keys.py
│ └── mail_agent.py
│
└── README.md
```

---

## ⚙️ Requirements

Dependencies:
streamlit
langchain
langchain-community
langchain-core
langchain-openai
langgraph
openai
python-dotenv


🧠 Example Workflow
```
Launch the app → The agent greets and asks for your name.
If you’re a new user → It requests your details and stores them.
If you’re an existing user → It loads your chat and booking history.
You can perform the following actions:
🔍 Search for hospitals/doctors
📅 Book appointments
📖 View bookings
❌ Cancel or reschedule existing ones
All your data persists locally and can be reloaded anytime.
```
🧑‍💻 Author
Devaraj Kudumula
