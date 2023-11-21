import time

import main
import streamlit as st
from openai import OpenAI

st.title("FT Insight")

client = OpenAI()
assistant_id = "asst_OyRLwTQFyByVaSZCbfxJRfAA"

# Create thread
thread = main.create_thread()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input(""):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    main.add_message_to_thread(thread.id, prompt)
    run = main.create_run(thread)

    with st.status("Running"):
        status = ""
        while run.completed_at is None:
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id
            )
            if run.status != status:
                st.write(run.status)
                st.write(run.instructions)
            time.sleep(2)

    messages = client.beta.threads.messages.list(thread_id=thread.id)
    message_list = list(messages)
    responses = []
    for i in message_list:
        for c in i.content:
            responses.append(c.text.value)
    # response = [i for i in messages if i.role == "assistant"]
    # response = [i.content for i in response]
    response = responses
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(len(response))
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
