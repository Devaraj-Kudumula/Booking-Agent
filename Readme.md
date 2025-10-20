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

