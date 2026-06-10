# NBA Chatbot

A simple rule-based NBA chatbot built in Python that answers questions about NBA teams, players, and the league.

## Features

* Detects user intent from natural language questions
* Identifies NBA teams and players from user input
* Returns team rankings and player rosters
* Provides information about NBA players and teams
* Uses a clean pipeline architecture:

  * Intent Detection
  * Entity Extraction
  * Decision Engine
  * Response Generation

## Example Questions

* Who plays for the Lakers?
* What is the ranking of the Knicks?
* Tell me about Stephen Curry.
* When did LeBron James join the Lakers?
* What is the NBA?

## Project Structure

* `data.py` — Contains NBA teams, players, league information, and fallback responses.
* `chatbot.py` — Main chatbot logic including intent detection, entity extraction, and response generation.

## Technologies Used

* Python
* Dictionaries and nested data structures
* Rule-based natural language processing

## Future Improvements

* Add support for all NBA teams and players
* Improve intent detection with machine learning
* Integrate live NBA data through an API
* Add player statistics and team records
* Implement fuzzy matching for misspelled names

## How to Run

1. Clone the repository.
2. Make sure Python 3 is installed.
3. Run:

```bash
python chatbot.py
```

4. Enter an NBA-related question when prompted.

## Author

Bahareh Saidi
