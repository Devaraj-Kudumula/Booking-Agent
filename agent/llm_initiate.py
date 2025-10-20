from langchain_openai import AzureChatOpenAI, ChatOpenAI
from utils.llm_keys import args, api_key

def get_llm():
    llm = AzureChatOpenAI(**args)
    return llm

def get_openai_llm():
    llm = ChatOpenAI(api_key=api_key, temperature=0.1, top_p=0.1, model_name="gpt-4")
    return llm