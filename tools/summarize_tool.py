from langchain.tools import tool
from utils.config import get_llm

llm = get_llm()

@tool
def summarize_tool(text: str) -> str:
    """
    Summarizes the given text into key points.
    """

    prompt=f"""
    You are a helpful assistant.

    Summarize the following information into:
    - key trends
    - Top companies 
    - Main insights

    Guidelines:
    - Extract relevant entities accurately
    - keep the output structured and concise
    - Do not assume missing information

    Text:
    {text}
    """

    response = llm.invoke(prompt)

    return response.content