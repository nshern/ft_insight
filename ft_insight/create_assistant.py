import glob
from typing import List

from openai import OpenAI
from tqdm import tqdm

client = OpenAI()


def get_files(directory):
    return glob.glob(f"{directory}/*.txt", recursive=True)


def create_assistant(
    name: str, instructions: str, tools: List[str], model: str
) -> None:
    files = get_files("./files")

    ids = []
    for file in tqdm(files):
        file = client.files.create(file=open(file, "rb"), purpose="assistants")
        ids.append(file.id)

    allowed_tools = ["retrieval", "code_interpreter", "function"]
    for tool in tools:
        if tool not in allowed_tools:
            raise ValueError(
                f"Invalid tool: {tool}. Allowed tools are {allowed_tools}"
            )

    tools_formatted = [{"type": f"{i}"} for i in tools]

    client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools_formatted,  # type: ignore
        model=model,
        file_ids=ids,
    )

    print(f"Successfully created {name}")


if __name__ == "__main__":
    create_assistant(
        name="FT Insight",
        instructions="You are an expert in danish politics.\
         Answer questions related to folketingets meeting minutes.\
         You may ONLY communicate in Danish.\
         Under no circumstances may you communicate in any other language.",
        tools=["retrieval", "code_interpreter"],
        model="gpt-4-1106-preview",
    )
