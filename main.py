from agents.agent import get_agent
if __name__ == "__main__":
    agent = get_agent()

    query = "latest trends in electric vehicles and top EV companies like Tesla BYD Volkswagen"

    result = agent.invoke({"input": query})

    print("\n" + "="*50)
    print("Final Answer")
    print("="*50)

    print("\n" + result['output'])

    print("\n" + "="*50)