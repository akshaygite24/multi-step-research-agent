from agents.agent import get_agent

agent = get_agent()

def run_agent(query):
    result = agent.invoke({"input": query})
    
    return result['output']