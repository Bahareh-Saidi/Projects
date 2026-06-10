from data import data, fallback

intents = {
    "team_ranking": ["ranking", "rank", "position", "standing"],
    "team_players": ["players", "roster", "lineup", "who plays"],
}


# Detect intent
def detect_intent(text):
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in text:
                return intent
    return None


# Extract entity
def extract_entity(text):

    name_map = {
        "teams": {
            "knicks": "new york knicks",
            "la lakers": "los angeles lakers",
            "lakers": "los angeles lakers",
            "warriors": "golden state warriors",
            "celtics": "boston celtics",
            "nuggets": "denver nuggets",
            "bucks": "milwaukee bucks",
            "suns": "phoenix suns",
            "mavericks": "dallas mavericks",
            "heat": "miami heat"
        },
        "players": {
            "jalen brunson": "jalen brunson",
            "lebron": "lebron james",
            "james": "lebron james",
            "curry": "stephen curry",
        },
    }

    # Teams
    for phrase, team in name_map["teams"].items():
        if phrase in text:
            return {
                "type": "team",
                "value": team
            }

    # Players
    for phrase, player in name_map["players"].items():
        if phrase in text:
            return {
                "type": "player",
                "value": player
            }

    # League
    if "nba" in text:
        return {
            "type": "league",
            "value": "nba"
        }

    return None


# Decision engine
def decide(intent, entity):

    if not entity:
        return fallback

    # Team logic
    if entity["type"] == "team":

        if intent == "team_ranking":
            return data["teams"][entity["value"]]["ranking"]

        elif intent == "team_players":
            return data["teams"][entity["value"]]["players"]

        else:
            return data["teams"][entity["value"]]

    # Player logic
    elif entity["type"] == "player":
        return data["players"][entity["value"]]

    # League logic
    elif entity["type"] == "league":
        return data["league"]

    return fallback


# Chatbot
def chatbot():

    text = input("Ask any question about NBA: ").lower()

    intent = detect_intent(text)
    entity = extract_entity(text)

    response = decide(intent, entity)

    print(response)


chatbot()