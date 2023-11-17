import time

from openai import OpenAI

client = OpenAI()
assistant_id = "asst_OyRLwTQFyByVaSZCbfxJRfAA"

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Hvad kan du fortælle mig om mødereferaterne?",
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

print("Complete!")
messages = client.beta.threads.messages.list(thread_id=thread.id)

# TODO: Extract message response
print(messages)
# TODO: Create loop that enables continous conversation
# TODO: Put into streamlit app
