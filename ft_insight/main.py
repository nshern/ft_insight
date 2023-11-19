import time

from openai import OpenAI

client = OpenAI()
assistant_id = "asst_OyRLwTQFyByVaSZCbfxJRfAA"

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hvilken person har talt mest på møderne?",
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant_id,
    instructions="Du må KUN tale dansk",
)

messages = client.beta.threads.messages.list(thread_id=thread.id)

run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

while run.completed_at is None:
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    time.sleep(2)

messages = client.beta.threads.messages.list(thread_id=thread.id)

for i in messages:
    role = i.role
    for c in i.content:
        print(f"{role}: {c.text.value}")  # type: ignore


# TODO: Create loop that enables continous conversation
# TODO: Put into streamlit app
