🩺 Smart Medical Booking Agent
    An intelligent AI-powered medical appointment assistant built with LangGraph / LangChain and Streamlit.


🚀 Features
    👤 User Onboarding
        Input Details: user name, email, phone, and region.
        Stores data in users.json.
    🧠 AI Agent (LangChain / LangGraph)
    Uses a React-style chat agent created using langgraph with access to the following tools:
        🔍 discover_hospitals — To find nearest hospitals/doctors.
        📅 book_appointment — To book new medical appointments.
        📖 view_bookings — to view user’s active/past bookings.
        ❌ cancel_user_booking — to cancel or reschedule the existing bookings.
    💾 Persistent Memory
    Chat history and user details are stored locally:
    data/users.json → user details
    data/chat_history.json → chat logs



🧰 Tech Stack
| Layer             | Technology                                      |
|-------------------|-------------------------------------------------|
| 💻 Frontend       | Streamlit                                       |
| 🧠 Agent Framework | LangChain / LangGraph                           |
| 🧩 Language Model  | OpenAI GPT (AzureChatOpenAI, ChatOpenAI)        |
| 📂 Storage         | Local JSON files (no database)                  |
| ✉️ Communication   | Simulated Email Tool Calls                      |

🏗️ Project Structure
smart-medical-booking-agent/
│
├── app.py                        
│
├── agent/
│   ├── main_agent.py  
│   ├── llm_initiate.py              
│   ├── memory_manager.py
│   ├── schemas.py          
│   ├── tool_functions.py
│   └── tools.py  
│
├── data/
│   ├── users.json
|   ├── bookings.json   
|   ├── input_prompt.py                
│   └── chat_history.json      
│
├── utils/
│   ├── llm_keys.py
│   └── mail_agent.py 
└── README.md


NOTES:
    - created llm to be accessed with either ChatOpenAI(openai_fkeys), AzureChatOpenAI(Azure deployment keys)
    - add the keys in llm_keys.py
    - change the get_llm() in main_agent and mail_agent to access llms.
    - Start of converstion agent asks for user name (case-sensitive) if user details not found, asks for user details else loads the chat screen.
    - all the chat history is stored in chat_hsitory.json against user name.
    - all the bookings are stored in bookings.json, if booking is cancelled, status of the booking changes to `cancelled` but the booking reference is still there.
    - used langgraph to create the agents,
        - all the tools are created from fuctions using StructedTool function, schemas helps llm to identify the input_parameters of the tools properly and call the tool with all the needed inputs.


Requirements

streamlit
langchain
langchain-community
langchain-core
langchain-openai 
langgraph
openai
python-dotenv
