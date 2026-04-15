from tools.search_tool import get_search_tool
from tools.summarize_tool import summarize_tool

if __name__ == "__main__":
    search_tool = get_search_tool()

    query = "latest trends in electric vehicles and top EV companies like Tesla BYD Volkswagen"
    raw_result = search_tool.run(query)
    print("Raw Results:\n", raw_result)

    summary = summarize_tool.invoke(raw_result)
    print("\n\nSummarizes Result: \n", summary)
    