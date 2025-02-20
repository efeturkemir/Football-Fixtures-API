from fastapi import FastAPI
from app.fetch_super_league import fetch_super_league_fixtures
from app.fetch_premier_league import fetch_premier_league_fixtures
from app.fetch_bundesliga import fetch_bundesliga_fixtures
from app.fetch_laliga import fetch_laliga_fixtures
from app.fetch_seriea import fetch_seriea_fixtures
from app.fetch_all_leagues import fetch_match_fixtures

app = FastAPI()


LEAGUE_URLS = {
    "super_league": "https://www.tff.org/default.aspx?pageID=198",
    "premier_league": "https://onefootball.com/en/competition/premier-league-9/fixtures",
    "bundesliga": "https://onefootball.com/en/competition/bundesliga-1/fixtures",
    "la_liga": "http://onefootball.com/en/competition/laliga-10/fixtures",
    "serie_a": "https://onefootball.com/en/competition/serie-a-13/fixtures"
}


@app.get("/matches/{league_name}")
async def get_league_matches(league_name: str):
    league_name = league_name.lower()
    
    if league_name == "super_league":
        matches = fetch_super_league_fixtures()
    elif league_name in LEAGUE_URLS:
        url = LEAGUE_URLS[league_name]
        matches = fetch_match_fixtures(url, league_name)
    else:
        return {"error": "Invalid league name"}

    return {"matches": matches}

