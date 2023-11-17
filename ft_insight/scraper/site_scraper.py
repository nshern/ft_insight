import glob
import os
import uuid
from typing import List

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Fetch the content from the URL
response = requests.get(
    "https://www.ft.dk/da/dokumenter/dokumentlister/referater?"
    "numberOfDays=-365&pageSize=200&totalNumberOfRecords=89"
)


def get_urls() -> List[str]:
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all the <tr> tags
        tr_tags = soup.find_all("tr")

        links = []

        # Print or process the <tr> tags as needed
        for tr in tr_tags:
            if "forhandlinger" in str(tr):
                s = str(tr)
                s = s.split("data-url=")
                for i in s:
                    if "forhandlinger" in i:
                        k = i.splitlines()
                        links.append(
                            f'https://www.ft.dk{(k[0].split(" ")[0])}'
                        )
                        links = [i.replace('"', "") for i in links]
        return links

    else:
        print(f"Failed to fetch the page, status code: {response.status_code}")
        return []


def get_text(text):
    soup = BeautifulSoup(text, "html.parser")

    for script in soup(
        ["script", "style"]
    ):  # Remove script and style elements
        script.extract()

    # Get text from the soup object and preserve paragraphs
    text_with_paragraphs = ""
    for paragraph in soup.find_all(["p", "br"]):
        if paragraph.name == "br":
            text_with_paragraphs += "\n"
        else:
            text_with_paragraphs += "\n\n" + paragraph.get_text()

    return text_with_paragraphs


def get_plain_texts():
    plain_texts = []
    urls = get_urls()
    for url in tqdm(urls):
        r = requests.get(url)
        r.encoding = "utf-8"
        plain_text = get_text(r.text)
        plain_texts.append(plain_text)

    return plain_texts


def save_plain_texts(dir):
    texts = get_plain_texts()
    for i in tqdm(texts):
        with open(f"{dir}/{uuid.uuid4()}.txt", "w") as f:
            f.write(i)


def clear_dir(dir):
    files = glob.glob(os.path.join(dir, "*"))
    # Check if files are not empty and send a little message.
    for file_path in files:
        try:
            if os.path.isfile(
                file_path
            ):  # Make sure it's a file, not a directory
                os.remove(file_path)
        except Exception as e:
            print(
                f"Error occurred while deleting file: {file_path}. Error: {e}"
            )


def main():
    clear_dir("./data")
    save_plain_texts("./data")


if __name__ == "__main__":
    main()
