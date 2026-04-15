import streamlit as st
from agent_runner import run_agent

st.set_page_config(page_title="AI Research Agent")

st.title("Multi-Step Research Agent")

st.write("Ask anything about trends, companies and topics!")

query = st.text_input("Enter your Query:")

if st.button("Run Agent"):
    if query:
        with st.spinner("Thinking..."):
            result = run_agent(query)

        st.subheader("Result")
        st.write(result)
    else:
        st.warning("Please enter a Query!")