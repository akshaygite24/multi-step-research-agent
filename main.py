from agent_runner import run_agent

if __name__ == "__main__":

    while True:
        query = input("\n\nEnter Query or exit:\n")
        if query.lower() == "exit":
            print("Exiting...")
            break
    
        if query.strip():
            output = run_agent(query)
            print("\nResult:\n")
            print(output)
        else:
            print("Please enter a Valid Query!")