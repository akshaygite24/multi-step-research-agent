# Multi-Step Research Agent

## Overview

This project is an AI-based research agent that performs web search, processes results, and generates structured summaries.
It uses a multi-step reasoning approach (ReAct pattern) to decide which tools to use.

## Features

* Web search using DuckDuckGo
* LLM-based summarization using Groq
* Multi-step reasoning with LangChain agents
* Modular project structure
* Streamlit based user-inteface

## Project Structure

```
multi-step-research-agent/
│── app.py              # Streamlit UI
│── main.py             # CLI entry for testing agent
│── agent_runner.py     # Reusable Agent Execution Logic
│
│── agents/
│     ├── agent.py
│
│── tools/
│     ├── search_tool.py
│     ├── summarize_tool.py
│
│── utils/
│     ├── config.py
```

## Setup

1. Clone the repository

```
git clone https://github.com/your-username/multi-step-research-agent.git
cd multi-step-research-agent
```

2. Create and activate virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create a `.env` file and add your API key

```
GROQ_API_KEY=your_api_key_here
```

## Running the Project

Run Streamlit app:

```
streamlit run app.py
```

Run via CLI:

```
python main.py
```

## Example Query

```
Latest trends in electric vehicles and top companies
```

## Tech Stack

* Python
* LangChain
* Groq
* DuckDuckGo Search
* Streamlit

## Future Improvements

* Add memory support
* Improve UI
* Integrate RAG

