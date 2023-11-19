# FT Insight

This project is an attempt at recreating [polGPT](https://github.com/emillykkejensen/polGPT) using the OpenAI [Assistants API](https://platform.openai.com/docs/assistants/overview)

## Install
git clone this repo

## Usage
Set OpenAI api key as environment variable

### Set up environment variable
bash, sh, zsh
```
export OPENAI_API_KEY=[Insert sertapi key]
```

or fish
```
set -Ux OPENAI_API_KEY [Insert open ai api key]
```

### Install dependencies
```
cd to/folder/path
poetry install
```

### Run CLI
```
python main.py
```

## Acknowledgments
- [polGPT](https://github.com/emillykkejensen/polGPT)
