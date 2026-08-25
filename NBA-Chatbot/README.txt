# 🏀 NBA Chatbot

A Python-based conversational NBA chatbot that understands natural language questions about NBA teams, players, and the league.

The chatbot uses a rule-based natural language processing pipeline to identify what the user is asking, extract relevant NBA entities, and generate an appropriate response.

## Features

- Detects user intent from natural language questions
- Extracts NBA teams and players from user input
- Provides information about NBA teams and players
- Returns team rankings and player rosters
- Handles general NBA questions
- Uses a modular chatbot pipeline:
  - Intent Detection
  - Entity Extraction
  - Decision Engine
  - Response Generation

## How It Works

The chatbot processes each user question through several stages:

```text
User Input
    ↓
Intent Detection
    ↓
Entity Extraction
    ↓
Decision Engine
    ↓
Response Generation
1. Intent Detection

The chatbot analyzes the user's question to determine what type of information they are requesting.

Examples include:

Player information
Team information
Team rankings
Player rosters
General NBA information
2. Entity Extraction

After identifying the intent, the chatbot determines which NBA entity the user is referring to.

For example:

"Who plays for the Lakers?"

The chatbot identifies:

Intent: Team Roster
Entity: Los Angeles Lakers
3. Decision Engine

The decision engine combines the detected intent and extracted entity to determine which response should be returned.

4. Response Generation

The chatbot generates a response using the available NBA data and fallback responses when the requested information cannot be found.

Example Questions

The chatbot can respond to questions such as:

Who plays for the Lakers?

What is the ranking of the Knicks?

Tell me about Stephen Curry.

When did LeBron James join the Lakers?

What is the NBA?
Project Structure
NBA-Chatbot/
│
├── chatbot.py      # Main chatbot logic
├── frontend.py     # User interface
├── README.txt      # Project documentation
└── .gitignore      # Git configuration
Technologies
Python
Rule-based Natural Language Processing
Dictionaries and nested data structures
Entity extraction
Intent classification
Key Concepts

This project demonstrates several core software engineering and NLP concepts:

Natural language processing
Intent classification
Entity extraction
Data modeling
Modular program design
Input validation
Decision logic
Exception and fallback handling
Getting Started
Prerequisites

Make sure Python 3 is installed on your system.

Clone the Repository
git clone https://github.com/Bahareh-Saidi/Projects.git
cd Projects/NBA-Chatbot
Run the Chatbot
python chatbot.py

Enter an NBA-related question when prompted.

Future Improvements

Potential improvements include:

Support for all NBA teams and players
Integration with a live NBA statistics API
Real-time player and team statistics
Machine learning-based intent detection
Fuzzy matching for misspelled player and team names
Expanded conversational capabilities
Persistent conversation context


Author
Bahareh Saidi