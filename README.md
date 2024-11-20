# JOI - a personal voice assistant
A project inspired by the movie "Blade Runner 2049"

![alt text](https://i.redd.it/winjsl2x90891.jpg)

## Table of Contents
- [JOI - a personal voice assistant](#joi---a-personal-voice-assistant)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Getting API keys](#getting-api-keys)
  - [Usage](#usage)
  - [License](#license)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/Navfalbek/Joi-assistant.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Getting API keys
In the project there were used several APIs. Which are:
1. Picovoice access tokens for Wake word detections and Speech-Instanse commands, can be taken from [Picovoice.ai](https://picovoice.ai/docs/api/picovoice-python/)
2. Spotify API keys and can be taken from [Developers Spotify](https://developer.spotify.com/)
3. OpenAI tokens and can be taken from [OpenAI](https://openai.com/index/openai-api/)
4. Google Gmail tokens in order to manage and get unread messages from inbox, can be taken from [Developers Google](https://developers.google.com/gmail/api/guides)

## Usage
Simply run:
```bash
python main.py
```

## License
This project is licensed under the [MIT License](LICENSE).
