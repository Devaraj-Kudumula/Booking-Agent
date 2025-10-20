from langchain_openai import AzureChatOpenAI
from agent.llm_initiate import get_llm

def mailing_agent(booking_details: dict) -> str:
    llm = get_llm()
    template = """You are an expert in writing emails. create a professional email to the user about their appointment booking with the following details:
    "id": {booking_id},
    "user_name": {user_name},
    "user_email": {user_email},
    "hospital": {hospital_name},
    "doctor": {doctor_name},
    "date": {date},
    "time": {time},
    "status": {status},"""
    
    prompt_text = template.format(booking_id=booking_details["id"], 
                                 user_name=booking_details["user_name"],
                                 user_email=booking_details["user_email"],
                                 hospital_name=booking_details["hospital"],
                                 doctor_name=booking_details["doctor"],
                                 date=booking_details["date"],
                                 time=booking_details["time"],
                                 status=booking_details["status"])
    response = llm.invoke(prompt_text)
    return response