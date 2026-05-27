from data import data, fallback

intents = {
    "team_ranking": ["ranking", "rank", "position", "standing"],
    "team_players": ["players", "roster", "lineup", "who plays"],
}


# Detenct the intents
def detect_intent(text):
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
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
        if phrase in user_input and team in data["teams"]:
            if intent == "team_ranking":
                return data["teams"][team]["ranking"]
            elif intent == "team_players":
                return data["teams"][team]["players"]
            else:
                return data["teams"][team]
            found = True
            break

    # Players
    if not found:
        for phrase, player in name_map["players"].items():
            if phrase in user_input and player in data["players"]:
                return data["players"][player]
                found = True
                break


# 2. WORD MATCHING
if not found:
    for word in words:

        # Team
        if word in name_map["teams"]:
            team = name_map["teams"][word]
            if team in data["teams"]:
                if intent == "team_ranking":
                    print(data["teams"][team]["ranking"])
                elif intent == "team_players":
                    print(data["teams"][team]["players"])
                else:
                    print(data["teams"][team])
                found = True
                break

        # Player
        elif word in name_map["players"]:
            player = name_map["players"][word]
            if player in data["players"]:
                print(data["players"][player])
                found = True
                break

        # League
        elif word in data["league"]:
            print(data["league"][word])
            found = True
            break


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
