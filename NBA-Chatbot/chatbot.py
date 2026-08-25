from datetime import datetime

from nba_api.stats.static import teams, players

from nba_api.stats.endpoints import (
    commonallplayers,
    commonplayerinfo,
    commonteamroster,
    leaguestandings,
    leaguedashplayerstats,
    leaguedashteamstats,
    playercareerstats,
)

# ---------------------------------------------------------
# SETTINGS
# ---------------------------------------------------------

LEAGUE_ID = "00"


def format_section(title, lines):
    cleaned = [str(line) for line in lines if line is not None]
    if not cleaned:
        return title

    width = max(len(title), max(len(str(line)) for line in cleaned))
    divider = "-" * width
    return "\n".join([title, divider, *cleaned])


def format_kv(title, data):
    lines = [f"{title}"]
    for key, value in data.items():
        lines.append(f"{key}: {value}")
    return format_section(title, lines[1:])


# ---------------------------------------------------------
# SEASON
# ---------------------------------------------------------


def get_current_season():
    """
    NBA season changes in October.

    August 2026 -> 2025-26
    November 2026 -> 2026-27
    """

    now = datetime.now()

    if now.month >= 10:
        start_year = now.year
    else:
        start_year = now.year - 1

    return f"{start_year}-{str(start_year + 1)[-2:]}"


# ---------------------------------------------------------
# TEAM SEARCH
# ---------------------------------------------------------


def find_team(text):

    text = text.lower().strip()

    all_teams = teams.get_teams()

    # Exact full-name match
    for team in all_teams:
        if team["full_name"].lower() == text:
            return team

    # Full name contained in question
    for team in all_teams:
        if team["full_name"].lower() in text:
            return team

    # City
    for team in all_teams:
        if team["city"].lower() in text:
            return team

    # Nickname
    for team in all_teams:
        if team["nickname"].lower() in text:
            return team

    # Abbreviation
    for team in all_teams:
        if team["abbreviation"].lower() in text:
            return team

    return None


# ---------------------------------------------------------
# PLAYER SEARCH
# ---------------------------------------------------------


def find_player(text):

    text = text.lower().strip()

    all_players = players.get_active_players()

    # Exact name
    for player in all_players:
        if player["full_name"].lower() == text:
            return player

    # Full name contained in question
    for player in all_players:
        if player["full_name"].lower() in text:
            return player

    # First + last name search
    words = text.split()

    for player in all_players:

        player_words = player["full_name"].lower().split()

        if all(word in words for word in player_words):
            return player

    return None


# ---------------------------------------------------------
# ALL TEAMS
# ---------------------------------------------------------


def get_all_teams():

    all_teams = teams.get_teams()

    output = ["NBA TEAMS"]

    for team in all_teams:
        output.append(f"{team['full_name']:<26} ({team['abbreviation']})")

    return format_section("NBA TEAMS", output[1:])


# ---------------------------------------------------------
# ALL CURRENT PLAYERS
# ---------------------------------------------------------


def get_all_players():

    season = get_current_season()

    try:

        response = commonallplayers.CommonAllPlayers(
            is_only_current_season=1, league_id=LEAGUE_ID, season=season, timeout=10
        ).get_dict()

        dataset = response["resultSets"][0]

        headers = dataset["headers"]
        rows = dataset["rowSet"]

        columns = {name: index for index, name in enumerate(headers)}

        output = [f"CURRENT NBA PLAYERS ({season})"]

        for row in rows:

            player_name = row[columns["DISPLAY_FIRST_LAST"]]

            team_city = row[columns["TEAM_CITY"]]

            team_name = row[columns["TEAM_NAME"]]

            if team_name:
                output.append(f"{player_name:<24} - {team_city} {team_name}")
            else:
                output.append(player_name)

        return format_section(f"CURRENT NBA PLAYERS ({season})", output[1:])

    except Exception as error:

        return "I couldn't retrieve the current NBA players.\n" f"Error: {error}"


# ---------------------------------------------------------
# TEAM ROSTER
# ---------------------------------------------------------


def get_team_roster(team):

    season = get_current_season()

    try:

        response = commonteamroster.CommonTeamRoster(
            team_id=team["id"], season=season, league_id_nullable=LEAGUE_ID, timeout=10
        ).get_dict()

        dataset = response["resultSets"][0]

        headers = dataset["headers"]
        rows = dataset["rowSet"]

        columns = {name: index for index, name in enumerate(headers)}

        output = [f"Season: {season}"]

        for row in rows:

            name = row[columns["PLAYER"]]

            number = row[columns["NUM"]]

            position = row[columns["POSITION"]]

            height = row[columns["HEIGHT"]]

            weight = row[columns["WEIGHT"]]

            age = row[columns["AGE"]]

            experience = row[columns["EXP"]]

            school = row[columns["SCHOOL"]]

            output.append(
                f"{name:<22} | #{number:<2} | {position:<3} | {height} | {weight} | "
                f"Age {age} | Exp {experience} | {school}"
            )

        return format_section(f"{team['full_name']} ROSTER", output)

    except Exception as error:

        return (
            f"I couldn't retrieve the "
            f"{team['full_name']} roster.\n"
            f"Error: {error}"
        )


# ---------------------------------------------------------
# TEAM STANDINGS
# ---------------------------------------------------------


def get_team_standings(team):

    season = get_current_season()

    try:

        response = leaguestandings.LeagueStandings(
            league_id=LEAGUE_ID, season=season, season_type="Regular Season", timeout=10
        ).get_dict()

        dataset = response["resultSets"][0]

        headers = dataset["headers"]
        rows = dataset["rowSet"]

        columns = {name: index for index, name in enumerate(headers)}

        for row in rows:

            team_name = f"{row[columns['TeamCity']]} " f"{row[columns['TeamName']]}"

            if team_name.lower() == team["full_name"].lower():

                return format_section(
                    f"{team_name} STANDINGS",
                    [
                        f"Season: {season}",
                        f"Conference: {row[columns['Conference']]}",
                        f"Conference Rank: {row[columns['PlayoffRank']]}",
                        f"Record: {row[columns['Record']]}",
                        f"Streak: {row[columns['strCurrentStreak']]}",
                    ],
                )

        return "Team not found in standings."

    except Exception as error:

        return "I couldn't retrieve the standings.\n" f"Error: {error}"


# ---------------------------------------------------------
# PLAYER INFORMATION
# ---------------------------------------------------------


def get_player_info(player):

    try:

        response = commonplayerinfo.CommonPlayerInfo(
            player_id=player["id"], league_id_nullable=LEAGUE_ID, timeout=10
        ).get_dict()

        dataset = response["resultSets"][0]

        headers = dataset["headers"]
        rows = dataset["rowSet"]

        if not rows:
            return "No player information found."

        columns = {name: index for index, name in enumerate(headers)}

        row = rows[0]

        return format_section(
            f"PLAYER: {row[columns['DISPLAY_FIRST_LAST']]}",
            [
                f"Team: {row[columns['TEAM_NAME']]}",
                f"Position: {row[columns['POSITION']]}",
                f"Height: {row[columns['HEIGHT']]}",
                f"Weight: {row[columns['WEIGHT']]}",
                f"Age: {row[columns['BIRTHDATE']]}",
                f"School: {row[columns['SCHOOL']]}",
                f"Country: {row[columns['COUNTRY']]}",
                f"Experience: {row[columns['SEASON_EXP']]} seasons",
                f"Draft Year: {row[columns['DRAFT_YEAR']]}",
                f"Draft Round: {row[columns['DRAFT_ROUND']]}",
                f"Draft Number: {row[columns['DRAFT_NUMBER']]}",
            ],
        )

    except Exception as error:

        return "I couldn't retrieve player information.\n" f"Error: {error}"


# ---------------------------------------------------------
# PLAYER SEASON STATS
# ---------------------------------------------------------


def get_player_stats(player):

    season = get_current_season()

    try:

        response = leaguedashplayerstats.LeagueDashPlayerStats(
            league_id=LEAGUE_ID,
            season=season,
            season_type_all_star="Regular Season",
            per_mode_detailed="PerGame",
            timeout=10,
        ).get_dict()

        dataset = response["resultSets"][0]

        headers = dataset["headers"]
        rows = dataset["rowSet"]

        columns = {name: index for index, name in enumerate(headers)}

        for row in rows:

            if row[columns["PLAYER_ID"]] == player["id"]:

                return format_section(
                    f"{row[columns['PLAYER_NAME']]} - {season}",
                    [
                        f"Games: {row[columns['GP']]}",
                        f"Minutes: {row[columns['MIN']]:.1f}",
                        f"Points: {row[columns['PTS']]:.1f}",
                        f"Rebounds: {row[columns['REB']]:.1f}",
                        f"Assists: {row[columns['AST']]:.1f}",
                        f"Steals: {row[columns['STL']]:.1f}",
                        f"Blocks: {row[columns['BLK']]:.1f}",
                        f"FG%: {row[columns['FG_PCT']]:.3f}",
                        f"3P%: {row[columns['FG3_PCT']]:.3f}",
                        f"FT%: {row[columns['FT_PCT']]:.3f}",
                        f"Turnovers: {row[columns['TOV']]:.1f}",
                        f"Plus/Minus: {row[columns['PLUS_MINUS']]:.1f}",
                    ],
                )

        return (
            f"No {season} statistics are currently "
            f"available for {player['full_name']}."
        )

    except Exception as error:

        return "I couldn't retrieve player statistics.\n" f"Error: {error}"


# ---------------------------------------------------------
# PLAYER CAREER STATS
# ---------------------------------------------------------


def get_player_career(player):

    try:

        response = playercareerstats.PlayerCareerStats(
            player_id=player["id"],
            per_mode36="PerGame",
            league_id_nullable=LEAGUE_ID,
            timeout=10,
        ).get_dict()

        dataset = response["resultSets"][0]

        headers = dataset["headers"]
        rows = dataset["rowSet"]

        columns = {name: index for index, name in enumerate(headers)}

        if not rows:
            return "No career statistics available."

        # Most recent season
        row = rows[-1]

        return format_section(
            f"{player['full_name']} CAREER DATA",
            [
                f"Games: {row[columns['GP']]}",
                f"Points: {row[columns['PTS']]:.1f}",
                f"Rebounds: {row[columns['REB']]:.1f}",
                f"Assists: {row[columns['AST']]:.1f}",
                f"Steals: {row[columns['STL']]:.1f}",
                f"Blocks: {row[columns['BLK']]:.1f}",
            ],
        )

    except Exception as error:

        return "I couldn't retrieve career statistics.\n" f"Error: {error}"


# ---------------------------------------------------------
# ANSWER QUESTION
# ---------------------------------------------------------


def answer_question(text):

    normalized = text.lower().strip()

    # -----------------------------------------------------
    # ALL TEAMS
    # -----------------------------------------------------

    if (
        "all teams" in normalized
        or "every team" in normalized
        or "list teams" in normalized
    ):
        return get_all_teams()

    # -----------------------------------------------------
    # ALL PLAYERS
    # -----------------------------------------------------

    if (
        "all players" in normalized
        or "every player" in normalized
        or "list players" in normalized
    ):
        return get_all_players()

    # -----------------------------------------------------
    # PLAYER
    # -----------------------------------------------------

    player = find_player(normalized)

    if player:

        if "career" in normalized or "career stats" in normalized:
            return get_player_career(player)

        if (
            "stats" in normalized
            or "statistics" in normalized
            or "averages" in normalized
            or "average" in normalized
        ):
            return get_player_stats(player)

        return get_player_info(player)

    # -----------------------------------------------------
    # TEAM
    # -----------------------------------------------------

    team = find_team(normalized)

    if team:

        if (
            "roster" in normalized
            or "players" in normalized
            or "who plays" in normalized
            or "who is on" in normalized
            or "who's on" in normalized
        ):
            return get_team_roster(team)

        if (
            "standing" in normalized
            or "standings" in normalized
            or "rank" in normalized
            or "ranking" in normalized
            or "record" in normalized
        ):
            return get_team_standings(team)

        # General team question:
        # Return current roster + standings.
        standings = get_team_standings(team)
        roster = get_team_roster(team)

        return f"{standings}\n\n{roster}"

    # -----------------------------------------------------
    # UNKNOWN
    # -----------------------------------------------------

    return (
        "I couldn't identify the NBA team or player. "
        "Try asking about a team, player, roster, "
        "standings, or statistics."
    )


# ---------------------------------------------------------
# TERMINAL MODE
# ---------------------------------------------------------


def chatbot():

    while True:

        text = input("Ask about basketball " "(or type 'quit'): ")

        if text.lower().strip() in {"quit", "exit"}:
            break

        print(answer_question(text))


# ---------------------------------------------------------
# RUN
# ---------------------------------------------------------

if __name__ == "__main__":
    chatbot()
