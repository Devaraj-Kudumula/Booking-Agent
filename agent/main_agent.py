from .tools import book_appointment_tool, view_bookings_tool, cancel_booking_tool, discover_hospitals_tool, get_mail_tool, get_date_time_tool
from .memory_manager import get_user_history
from typing import Literal
import random
from langgraph.checkpoint.memory import MemorySaver

from langgraph.graph import END,START, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode
from langchain_core.messages import SystemMessage, HumanMessage
from data.input_prompt import template
from .llm_initiate import get_llm

def get_llm_with_bind_tools():
    llm = get_llm()
    tools = get_tools()
    llm_with_tools = llm.bind_tools(tools)

    return llm_with_tools

def get_tools():
    return [
        book_appointment_tool,
        view_bookings_tool,
        cancel_booking_tool,
        discover_hospitals_tool,
        get_date_time_tool
    ]

def get_main_agent():
    llm_with_tools = get_llm_with_bind_tools()
    tools = get_tools()

    def should_continue(state: MessagesState) -> Literal["tools", END]:
        messages = state['messages']
        last_message = messages[-1]
        # If the LLM makes a tool call, then we route to the "tools" node
        if last_message.tool_calls:
            return "tools"
        # Otherwise, we stop (reply to the user)
        return END

    def call_model(state: MessagesState):
        print("Calling LLM with messages:")
        messages = state['messages']
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools)


    workflow = StateGraph(MessagesState)
    workflow.add_node("agent", call_model)
    workflow.add_node("tools", tool_node)
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges(
        "agent",
        should_continue,
    )
    workflow.add_edge("tools", 'agent')

    checkpointer = MemorySaver()

    app = workflow.compile(checkpointer)
    return app


import random
def get_output(agent_input):
    chat_history = get_user_history(user_name=agent_input['user_name'])
    processed_history = process_chat_history(chat_history)
    print("Chat History................:", chat_history)
    print("Agent Input................:", agent_input)
    print("...............................................................")
    app = get_main_agent()
    prompt = template.format(name=agent_input['user_name'],region=agent_input['region'],email=agent_input['user_email'])
    thread_val = random.randint(11,1000)
    config={"configurable": {"thread_id":thread_val}}
    input_msg = []
    input_msg = [SystemMessage(prompt)]
    input_msg.extend(processed_history)
    input_msg.append(HumanMessage(content=agent_input['question']))

    for output in app.stream({"messages": input_msg},
        config=config):
        print(output)
    final_response = format_response(output)
    return final_response

def format_response(result):
    final_response = result['agent']['messages'][0].content
    return final_response

def process_chat_history(chat_history):
    processed_history = []
    for msg in chat_history:
        if msg['ai']:
            processed_history.append(HumanMessage(content=msg['user']))
            processed_history.append(SystemMessage(content=msg['ai']))
        else:
            processed_history.append(HumanMessage(content=msg['user']))
    return processed_history