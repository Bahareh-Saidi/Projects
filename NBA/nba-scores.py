from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import leagueleaders

def get_scoreboard():
    ## API call happens
    ## Turns json into python dict
    data = scoreboard.ScoreBoard().get_dict()
    games = data['scoreboard']['games']

    if not games:
        print("No NBA games scheduled for today.")
        return

    for game in games:
        home = game['homeTeam']
        away = game['awayTeam']

        print("---------------------------------------")
        print(f"{home['teamTricode']} vs {away['teamTricode']}")
        print(f"{home['score']} - {away['score']}")
        print(f"Status: {game['gameStatusText']}")


# -----------------------------------------
# PLAYER STATS (PPG LEADERS)
# -----------------------------------------
def get_stats():
    data = leagueleaders.LeagueLeaders().get_dict()

    rows = data["resultSet"]["rowSet"]

    print("NBA Points Per Game Leaders:")
    for i, row in enumerate(rows[:10]):
        name = row[2]    # playerName
        ppg = row[23]    # PPG
        print(f"{i + 1}. {name} - {ppg} ppg")

get_scoreboard()
print()
get_stats()
