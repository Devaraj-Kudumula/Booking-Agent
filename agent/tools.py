from langchain_core.tools import StructuredTool
from .tool_functions import book_appointment, view_bookings, cancel_booking, discover_hospitals, get_mail, date_time_tool
from .schemas import BookAppointmentInput, ViewBookingsInput, CancelBookingInput, DiscoverHospitalsInput, GenerateEmailInput, DateTimeToolInput

book_appointment_tool = StructuredTool.from_function(
    func=book_appointment,
    name="book_appointment",
    description="Tool to Book an appointment with a doctor.",
    args_schema=BookAppointmentInput
)

view_bookings_tool = StructuredTool.from_function(
    func=view_bookings,
    name="view_bookings",
    description="Tool to View all bookings for a user.",
    args_schema=ViewBookingsInput
)

cancel_booking_tool = StructuredTool.from_function(
    func=cancel_booking,
    name="cancel_booking",
    description="Tool to Cancel an existing booking.",
    args_schema= CancelBookingInput
)

discover_hospitals_tool = StructuredTool.from_function(
    func=discover_hospitals,
    name="discover_hospitals",
    description="Tool to Discover nearest hospitals based on region and symptom or query",
    args_schema=DiscoverHospitalsInput
)

get_mail_tool = StructuredTool.from_function(
    func=get_mail,
    name="generate_email",
    description="Tool to Generate a professional email to confirm an appointment booking.",
    args_schema=GenerateEmailInput
)

get_date_time_tool = StructuredTool.from_function(
    func=date_time_tool,
    name="date_time_tool",
    description="Tool to Get the current date and time for a given timezone",
    args_schema=DateTimeToolInput
)