from openai import OpenAI

client = OpenAI()


def create_assistant():
    assistant = client.beta.assistants.create(
        name="Folketinget Insight",
        instructions="You are an expert in danish politics. \
        Answer questions related to folketingets meeting minutes. \
        You may ONLY communicate in Danish. \
        Under no circumstances may you communicate in any other language.",
        tools=[{"type": "code_interpreter"}],
        model="gpt-4-1106-preview",
    )

    return assistant


def create_thread():
    thread = client.beta.threads.create()
    return thread


def create_message(thread, content):
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=content,
    )
    return message
