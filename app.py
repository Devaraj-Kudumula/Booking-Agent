import streamlit as st
from agent.main_agent import get_output
from agent.memory_manager import get_user, add_user, add_message, get_user_history

st.set_page_config(page_title="Smart Medical Booking Agent", page_icon="🩺", layout="centered")
st.markdown("<h2 style='text-align:center;'>🩺 Smart Medical Booking Agent</h2>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "collect_details" not in st.session_state:
    st.session_state.collect_details = False
if st.session_state.user_name is None and not st.session_state.collect_details:
    name_input = st.text_input("Enter your name to start chatting:")
    if st.button("Start Chat"):
        user = get_user(name_input)
        if user:
            st.session_state.user_name = user["name"]
            st.session_state.chat_history = get_user_history(user["name"])
            st.success(f"Welcome back, {user['name']}!")
        else:
            st.warning("User not found. Let's collect your details first.")
            st.session_state.new_user_name = name_input
            st.session_state.collect_details = True
if st.session_state.collect_details:
    name = st.session_state.new_user_name
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    region = st.text_input("Region")
    if st.button("Save Details"):
        if not (email and phone and region):
            st.warning("Please fill all fields.")
        else:
            add_user(name, email, phone, region)
            st.session_state.user_name = name
            st.session_state.chat_history = []
            st.session_state.collect_details = False
            st.success(f"Welcome, {name}! Your onboarding completed successfully...")

if st.session_state.user_name and not st.session_state.collect_details:
    chat_container = st.container()
    with chat_container:
        if not st.session_state.chat_history:
            st.markdown("<p style='text-align:center; color:gray;'>Start chatting below 👇</p>",unsafe_allow_html=True,)
        else:
            for msg in st.session_state.chat_history[-10:]:
                if msg["user"]:
                    st.markdown(f"""<div style='text-align:right; margin-bottom:10px;'>
                            <div style="
                                display:inline-block;
                                background-color:#4CAF50;
                                color:white;
                                padding:10px 15px;
                                border-radius:18px;
                                max-width:70%;
                                font-size:16px;
                                word-wrap:break-word;">
                                <b>You:</b> {msg['user']}
                            </div></div>""",unsafe_allow_html=True,)
                if msg["ai"]:
                    st.markdown(f"""
                        <div style='text-align:left; margin-bottom:10px;'>
                            <div style="
                                display:inline-block;
                                background-color:#2f2f2f;
                                color:#f1f1f1;
                                padding:10px 15px;
                                border-radius:18px;
                                max-width:70%;
                                font-size:16px;
                                word-wrap:break-word;">
                                <b>AI:</b> {msg['ai']}
                            </div>
                        </div>""",unsafe_allow_html=True,)
    user_input = st.chat_input("Type your message ...")

    if user_input:
        user = get_user(st.session_state.user_name)
        add_message(st.session_state.user_name, "user", user_input)
        history_msgs = get_user_history(st.session_state.user_name)
        agent_input = {
            "user_name": user["name"],
            "user_email": user["email"],
            "region": user["region"],
            "question": user_input,
            "history": history_msgs,
        }

        response = get_output(agent_input)
        add_message(st.session_state.user_name, "ai", response)
        st.session_state.chat_history.append({"user": user_input, "ai": response})
        st.rerun()
