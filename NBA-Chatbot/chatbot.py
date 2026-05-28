from data import data, fallback

intents = {
    "team_ranking": ["ranking", "rank", "position", "standing"],
    "team_players": ["players", "roster", "lineup", "who plays"],
}


# Detenct the intents
def detect_intent(text): 
    for intent, keywords in intents.items(): 
        for keyword in keywords: 
            if keyword in text: 
                return intent 
    return None


# Entity extraction
def extract_entity(text):
    name_map = {
        "teams": {
            "knicks": "new york knicks",
            "la lakers": "los angeles lakers",
            "lakers": "los angeles lakers",
            "warriors": "golden state warriors",
        },
        "players": {
            "jalen brunson": "jalen brunson",
            "lebron": "lebron james",
            "james": "lebron james",
            "curry": "stephen curry",
        },
    }

    for phrase, team in name_map["teams"].items():
        if phrase in text and team in data["teams"]:
            return {
                "type": "team",
                "value": team
            }
            
    for phrase, player in name_map["players"].items():
        if phrase in text and player in data["players"]:
            return {
                type: "player",
                "value": player
            }
            
    if phrase in data["league"]:
        return {
            type: "league",
            "value": "nba"
        }


def decide(intent, entity, text):

    if intent == "team_ranking":
        return(data["teams"]entity["value"]["ranking"])
    elif intent == "team_players":
        return(data["teams"]entity["value"]["players"])
    else:
        return(data["teams"]entity["value"])

# Chatbot
def chatbot():
    text = input("Ask about movies: ").lower()

    intent = detect_intent(text)
    entity = extract_entity(text)
    found = False

    # default intent if missing
    if not intent and entity:
        print(fallback)

    response = decide(intent, entity)

    print(response)
