from tools.search_tool import get_search_tool


if __name__ == "__main__":
    search_tool = get_search_tool()

    query = "latest trend in electric vehicles and top companies"

    result = search_tool.run(query)

    print("Result:/n", result)