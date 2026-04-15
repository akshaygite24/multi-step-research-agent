from agent_runner import run_agent

if __name__ == "__main__":
    query = "latest trends in electric vehicles and top EV companies like Tesla BYD Volkswagen"

    output = run_agent(query)

    print(output)