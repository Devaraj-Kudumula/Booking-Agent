import json
import os

DATA_PATH = "data"

def load_json(filename):
    path = os.path.join(DATA_PATH, filename)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump([], f)
    with open(path, "r") as f:
        return json.load(f)

def save_json(filename, data):
    path = os.path.join(DATA_PATH, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def add_booking(booking):
    data = load_json("bookings.json")
    data.append(booking)
    save_json("bookings.json", data)

def get_user_bookings(user_email):
    data = load_json("bookings.json")
    return [b for b in data if b["user_email"] == user_email]

def cancel_booking(user_email, booking_id):
    data = load_json("bookings.json")
    for b in data:
        if b["user_email"] == user_email and b["id"] == booking_id:
            b["status"] = "cancelled"
    save_json("bookings.json", data)

def onboard_user(name, region, email):
    users = load_json("users.json")
    for u in users:
        if u["email"] == email:
            return f"Welcome back, {u['name']} from {u['region']}!"
    new_user = {"name": name, "region": region, "email": email}
    users.append(new_user)
    save_json("users.json", users)
    return f"👋 Welcome {name} from {region}! You're successfully onboarded."

def get_user_by_email(email):
    users = load_json("users.json")
    for u in users:
        if u["email"] == email:
            return u
    return None

import os
import json

DATA_PATH = "data"

def ensure_file(filename, default_content):
    path = os.path.join(DATA_PATH, filename)
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default_content, f)
    return path

# --- Users ---
def load_users():
    return json.load(open(ensure_file("users.json", [])))

def save_users(users):
    json.dump(users, open(os.path.join(DATA_PATH, "users.json"), "w"), indent=4)

def get_user(name):
    users = load_users()
    for u in users:
        if u["name"].lower() == name.lower():
            return u
    return None

def add_user(name, email, phone, region):
    users = load_users()
    user = {"name": name, "email": email, "phone": phone, "region": region}
    users.append(user)
    save_users(users)

# --- Chat History ---
def load_chat_history():
    return json.load(open(ensure_file("chat_history.json", {})))

def save_chat_history(history):
    json.dump(history, open(os.path.join(DATA_PATH, "chat_history.json"), "w"), indent=4)

def add_message(user_name, role, message):
    history = load_chat_history()
    if user_name not in history:
        history[user_name] = []
    if role == "user":
        history[user_name].append({"user": message, "ai": None})
    else:
        # update last None ai message
        if history[user_name] and history[user_name][-1]["ai"] is None:
            history[user_name][-1]["ai"] = message
        else:
            history[user_name].append({"user": None, "ai": message})
    save_chat_history(history)

def get_user_history(user_name):
    history = load_chat_history()
    return history.get(user_name, [])
