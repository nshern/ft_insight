import time

import main
import streamlit as st
from openai import OpenAI

st.title("Echo Bot")

client = OpenAI()
assistant_id = "asst_OyRLwTQFyByVaSZCbfxJRfAA"

thread = main.create_thread()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Write something"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    main.add_message_to_thread(thread_id=thread.id, content=prompt)
    run = main.create_run(thread)

    while run.completed_at is None:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id, run_id=run.id
        )
        time.sleep(2)

    messages = client.beta.threads.messages.list(thread_id=thread.id)

    messages_list = list(messages)  # Convert to list

    for i in reversed(messages_list):
        role = i.role
        for c in i.content:
            response = c.text.value  # type: ignore

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )
