# LLM Conversation & Debate Simulator

## Overview

This project is a Python-based command-line application that allows users to interact with multiple Large Language Models (LLMs) through Ollama. It supports normal conversations as well as debate mode, where one model argues against the previous response, creating an AI-to-AI discussion.

All conversations are automatically saved to a text file for future reference.

---

## Features

- Supports multiple local LLMs using Ollama
- Interactive command-line interface
- Debate mode for AI vs AI discussions
- Conversation continuation mode
- Automatic conversation logging
- Simple and lightweight implementation
- Easy to extend by adding more models

---

## Technologies Used

- Python 3
- Requests Library
- Ollama API
- DeepSeek-R1
- Llama 3.2

---

## Project Structure

```
LLM-Conversation-Debate/
│── main.py
│── README.md
│── requirements.txt
│── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/LLM-Conversation-Debate.git
```

### 2. Navigate into the project

```bash
cd LLM-Conversation-Debate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Ollama

Make sure Ollama is installed and running.

Example:

```bash
ollama run deepseek-r1
```

or

```bash
ollama run llama3.2
```

---

## Running the Project

Run the application using:

```bash
python main.py
```

---

## How It Works

1. Enter a question.
2. Choose whether to enable Debate Mode.
3. Select the model for each round.
4. The selected model generates a response.
5. The next model can either continue the discussion or argue against the previous response.
6. The conversation continues until the user exits.
7. Every response is saved automatically in a log file.

---

## Example

```
Enter question:
Will AI replace software engineers?

Debate mode? (yes/no):
yes

Round 1
1 - Deepseek-R1
2 - Llama 3.2

Choose model:
1

Deepseek-R1:
AI will transform software development rather than replace engineers...

Round 2

Choose model:
2

Llama 3.2:
I disagree because software engineering requires creativity...
```

---

## Requirements

- Python 3.8+
- Ollama
- Requests library

Install dependency:

```bash
pip install requests
```

---

## Future Improvements

- Support additional LLMs
- Streaming responses
- GUI using Tkinter or PyQt
- Chat history management
- Export conversations to PDF
- Custom temperature and model settings

---

## Author

**Sai Manaswi**

GitHub: https://github.com/yourusername

---

## License

This project is intended for learning and educational purposes.