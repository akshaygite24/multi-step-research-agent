from langchain_classic.agents import create_react_agent, AgentExecutor
from langsmith import Client
from utils.config import get_llm
from tools.search_tool import get_search_tool
from tools.summarize_tool import summarize_tool


def get_agent():
    llm = get_llm()

    tools = [
        get_search_tool(),
        summarize_tool
    ]

    client = Client()
    prompt = client.pull_prompt("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False
    )

    return agent_executor