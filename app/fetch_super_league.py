from bs4 import BeautifulSoup
import requests
def fetch_super_league_fixtures():
    # Sending the request to the website
    url = 'https://www.tff.org/default.aspx?pageID=198'
    response = requests.get(url)
    matches = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        match_rows = soup.find_all('tr', class_='haftaninMaclariTr')

        for row in match_rows:
            date = row.find('span', id=lambda x: x and 'lblTarih' in x)
            time = row.find('span', id=lambda x: x and 'lblSaat' in x)
            home_team = row.find('td', class_='haftaninMaclariEv')
            away_team = row.find('td', class_='haftaninMaclariDeplasman')
            home_goals = row.find('span', id=lambda x: x and 'Label5' in x)
            away_goals = row.find('span', id=lambda x: x and 'Label6' in x)

            if date and time and home_team and away_team:
                home_team_name = home_team.get_text(strip=True)
                away_team_name = away_team.get_text(strip=True)

                match = {
                    "date": date.get_text(strip=True),
                    "time": time.get_text(strip=True),
                    "home_team": home_team_name,
                    "away_team": away_team_name,
                    "home_goals": int(home_goals.get_text(strip=True)) if home_goals and home_goals.get_text(strip=True).isdigit() else None,
                    "away_goals": int(away_goals.get_text(strip=True)) if away_goals and away_goals.get_text(strip=True).isdigit() else None,
                    "league": "Super Lig"
                }

                # Append match data to the list
                matches.append(match)
            else:
                print(f"Skipping a match due to missing data: {row}")
    else:
        print(f"Failed to retrieve the page, status code: {response.status_code}")

    return matches
