from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class BookAppointmentInput(BaseModel):
    user_name: str = Field(..., description="Name of the user")
    user_email: str = Field(..., description="Email of the user")
    hospital_name: str = Field(..., description="Name of the hospital")
    doctor_name: str = Field(..., description="Doctor or department name")
    date: str = Field(..., description="Appointment date")
    time: str = Field(..., description="Appointment time")

class ViewBookingsInput(BaseModel):
    user_email: str = Field(..., description="Email of the user")

class CancelBookingInput(BaseModel):
    user_email: str = Field(..., description="Email of the user")
    booking_id: str = Field(..., description="ID of the booking to cancel")

class DiscoverHospitalsInput(BaseModel):
    question: str = Field(..., description="user question and region to find relevant hospitals.")

class GenerateEmailInput(BaseModel):
    name: str = Field(..., description="Name of the user")
    hospital: str = Field(..., description="Name of the hospital")
    doctor: str = Field(..., description="Name of the doctor")
    time: str = Field(..., description="Appointment time")

class DateTimeToolInput(BaseModel):
    timezone: str = Field(..., description="The timezone to get the current date and time for.")
