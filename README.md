# Chat-Bot-With-POO

A fun and interactive chatbot implementation using Object-Oriented Programming (POO) in Python. This project demonstrates polymorphism through multiple bot personalities that respond differently to user interactions.

## 📋 Overview

This chatbot system features three different bot personalities, each with unique response styles:

- **ChatBot**: The standard bot with balanced responses
- **BotEngracado** (Funny Bot): A humorous bot that tells jokes and responds playfully
- **BotSerio** (Serious Bot): A formal and professional bot

The bot randomly selects a personality at startup and can switch between personalities during the conversation.

## ✨ Features

- **Object-Oriented Design**: Uses inheritance and polymorphism to implement different bot personalities
- **Random Bot Selection**: Automatically selects a random bot personality at startup
- **Dynamic Personality Switching**: Users can switch to a different bot personality during conversation
- **Interactive Conversations**: Responds to specific keywords like "oi" (hello) and "piada" (joke)
- **Joke Responses**: Each bot has its own collection of Portuguese jokes
- **User-Friendly Interface**: Simple command-line interface for interaction

## 🤖 Bot Personalities

### ChatBot (Base Class)
The base chatbot class with default responses:
- **Greetings**: Responds with "Olá!"
- **Jokes**: Tells programming and math-related jokes
- **Fallback**: Generic responses when it doesn't understand

### BotEngracado (Funny Bot)
A playful variant with humorous responses:
- **Greetings**: "Olá, humano!"
- **Jokes**: Animal and punny jokes in Portuguese
- **Fallback**: Humorous error messages

### BotSerio (Serious Bot)
A professional and formal variant:
- **Greetings**: "Olá, senhor(a)."
- **Jokes**: Refuses to joke while working
- **Fallback**: Formal and polite error messages

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Theo-Prado/Chat-Bot-With-POO.git
cd Chat-Bot-With-POO
```

2. No additional dependencies required - the project only uses Python's built-in `random` module.

### Running the Chatbot

Simply execute the script:
```bash
python CHATBOT.py
```

## 💬 Usage

Once the chatbot is running, you can interact with it:

```
Você: oi
ChatBot: Olá!

Você: piada
ChatBot: Por que o computador foi ao médico? Porque estava com vírus!

Você: trocar
(Bot personality changes randomly)

Você: sair
(Program exits)
```

### Commands

- **"oi"** - Greet the bot
- **"criador"** - show the name of the code creator
- **"piada"** - Request a joke
- **"trocar"** - Switch to a random bot personality
- **"sair"** - Exit the program
- Any other text will receive a fallback response

## 📚 Code Structure

```
CHATBOT.py
├── ChatBot (Base class)
│   ├── __init__(nome)
│   └── responder(mensagem)
├── BotEngracado (Inherits from ChatBot)
│   └── responder(mensagem) [Override]
├── BotSerio (Inherits from ChatBot)
│   └── responder(mensagem) [Override]
└── Main Program Loop
    ├── Bot instantiation
    ├── User input handling
    └── Conversation management
```

## 🎓 Learning Concepts

This project demonstrates several Object-Oriented Programming principles:

- **Inheritance**: `BotEngracado` and `BotSerio` inherit from `ChatBot`
- **Polymorphism**: Different bot classes override the `responder()` method
- **Encapsulation**: Bot state is managed within class instances
- **Abstraction**: Users interact with bots through a simple interface

## 🌐 Language

The chatbot responses are primarily in **Portuguese**.

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created by [Theo-Prado](https://github.com/Theo-Prado)

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

---

**Enjoy chatting with your POO-based chatbot!** 🎉
