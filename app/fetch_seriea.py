import requests
from bs4 import BeautifulSoup

def fetch_seriea_fixtures():
    link = "https://onefootball.com/en/competition/serie-a-13/fixtures"
    source = requests.get(link).text
    page = BeautifulSoup(source, "html.parser")

    # Extract the container with matches
    match_container = page.find_all("ul", class_="grid MatchCardsList_matches__8_UwB")
    fixtures = []

    # Extract match details from the container
    for match in match_container:
        match_items = match.find_all("a", class_="MatchCard_matchCard__iOv4G")

        for match_item in match_items:
            teams = match_item.find_all("span", class_="SimpleMatchCardTeam_simpleMatchCardTeam__name__7Ud8D")
            if len(teams) >= 2:
                home_team = teams[0].text.strip()
                away_team = teams[1].text.strip()

                # Extract match date and time
                date_element = match_item.find("time", class_="title-8-bold")
                date_time = date_element.text.strip() if date_element else "Unknown"

                time_element = match_item.find("time", class_="SimpleMatchCard_simpleMatchCard__infoMessage___NJqW")
                match_time = time_element.text.strip() if time_element else "TBD"

                # Extract goals
                goal_elements = match_item.find_all("span", class_="SimpleMatchCardTeam_simpleMatchCardTeam__score__UYMc_")
                home_goals = goal_elements[0].text.strip() if len(goal_elements) > 0 else None
                away_goals = goal_elements[1].text.strip() if len(goal_elements) > 1 else None

                # Convert goals to integers
                if home_goals and home_goals.isdigit():
                    home_goals = int(home_goals)
                else:
                    home_goals = None

                if away_goals and away_goals.isdigit():
                    away_goals = int(away_goals)
                else:
                    away_goals = None

                fixtures.append({
                    'home_team': home_team,
                    'away_team': away_team,
                    'date': date_time,
                    'time': match_time,
                    'home_goals': home_goals,
                    'away_goals': away_goals
                })

    return fixtures
