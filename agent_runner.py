from agents.agent import get_agent

agent = get_agent()

def run_agent(query):
    try:
        result = agent.invoke({"input": query})
        return result['output']
    except Exception as e:
        return f"Error: {str(e)}"