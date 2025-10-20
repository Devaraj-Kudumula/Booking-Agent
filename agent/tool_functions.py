import random
from .memory_manager import *
from langchain_community.utilities import GoogleSerperAPIWrapper
from .llm_initiate import get_llm
from typing import Dict, Any
from datetime import datetime
import pytz
from utils.mail_agent import mailing_agent


def book_appointment(
        user_name:str,
        user_email:str,
        hospital_name:str,
        doctor_name:str,
        time:str,
        date
    ) -> str:
    """Use this tool to book an appointment for the user.
    Parameters:
    - user_name (str): Name of the user.
    - user_email (int): email id of the user.
    - hospital_name (int): Hospital name that the user selected.
    - doctor_name (int): Doctor name that the user selected.
    - time (str): Time slot selected by the user.

    Returns:
    - str: Confirmation message with booking details.
    """
    # conflict check
    print("Checking for booking conflicts.........")
    bookings = load_json("bookings.json")
    for b in bookings:
        if b["user_email"] == user_email and b["date"]== date and b["time"] == time and b["status"] == "confirmed":
            return f"⚠️ Conflict detected! You already have a booking at {time}"

    booking_id = f"BKG{random.randint(1000,9999)}"
    booking = {
        "id": booking_id,
        "user_name": user_name,
        "user_email": user_email,
        "hospital": hospital_name,
        "doctor": doctor_name,
        "date": date,
        "time": time,
        "status": "confirmed",
    }
    add_booking(booking)
    mail_response = mailing_agent(booking)
    print("Mail Response: ", mail_response.content)
    return f"✅ Booking confirmed with {doctor_name} at {hospital_name} on {time}"

def view_bookings(
        user_email: str
        ) -> str:
    bookings = get_user_bookings(user_email)
    if not bookings:
        return "No bookings found."
    return "\n".join([f"{b['id']} | {b['doctor']} | {b['time']} | {b['status']}" for b in bookings])

def cancel_user_booking(
        user_email, 
        booking_id
    ):
    cancel_booking(user_email, booking_id)
    return f"Booking {booking_id} cancelled successfully."



def discover_hospitals(question):
    serper_api_key = "8a46c8ecdb405e3ed59ef2655fd7ec228f46792e"
    search_results = []

    search = GoogleSerperAPIWrapper(serper_api_key=serper_api_key)
    results = search.results(question)
        
    if not results.get('organic'):
        return [{"message": "No results found for the query."}]
    
    # Collecting structured results for Google
    for unit in results.get('organic', []):
        search_results.append({
            'title': unit.get('title', 'No Title'),
            'link': unit.get('link', 'No Link'),
            'snippet': unit.get('snippet', 'No Snippet')
        })
    
    return search_results

def get_mail(
        name, 
        hospital, 
        doctor, 
        time
    ):
    llm = get_llm()
    template = """You are an expert email composer. Compose a professional email to the user confirming their appointment booking with the following details:
    Name: {name}
    Hospital: {hospital}
    Doctor: {doctor}
    Time: {time}"""
    
    prompt_text = template.format(name=name, hospital=hospital, doctor=doctor, time=time)
    response = llm.invoke(prompt_text)
    return response



def date_time_tool(timezone: str) -> Dict[str, Any]:
    """
    Asynchronously gets the current date and time based on a given timezone.

    Parameters:
    - timezone (str): The timezone to get the current date and time for.

    Returns:
    - Dict[str, Any]: Contains "response" (the current date and time) and "sources".
    """
    try:
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        response = str(current_time)
    except Exception as err:
        response = f"Failed to get date and time for timezone {timezone}: {err}"
    return response