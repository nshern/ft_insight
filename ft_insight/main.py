import os
import time

from openai import OpenAI

client = OpenAI()
assistant_id = "asst_OyRLwTQFyByVaSZCbfxJRfAA"


def create_thread():
    thread = client.beta.threads.create()
    return thread


def add_message_to_thread(thread_id, content):
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=content,
    )


def create_run(thread):
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
        instructions="Du må KUN tale dansk",
    )

    return run


def main():
    thread = create_thread()
    while True:
        content = input("user: ")

        add_message_to_thread(thread.id, content)
        run = create_run(thread)

        while run.completed_at is None:
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id
            )
            time.sleep(2)

        messages = client.beta.threads.messages.list(thread_id=thread.id)

        messages_list = list(messages)  # Convert to list
        os.system("clear")
        for i in reversed(messages_list):
            role = i.role
            for c in i.content:
                print(f"{role}: {c.text.value}")  # type: ignore


if __name__ == "__main__":
    main()
