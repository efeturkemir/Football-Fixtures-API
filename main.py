from fastapi import FastAPI
from app.fetch_all_leagues import fetch_match_fixtures

app = FastAPI()


LEAGUE_URLS = {
    "super_league": "https://onefootball.com/en/competition/sueper-lig-8/fixtures",
    "premier_league": "https://onefootball.com/en/competition/premier-league-9/fixtures",
    "bundesliga": "https://onefootball.com/en/competition/bundesliga-1/fixtures",
    "la_liga": "http://onefootball.com/en/competition/laliga-10/fixtures",
    "serie_a": "https://onefootball.com/en/competition/serie-a-13/fixtures"
}


@app.get("/matches/{league_name}")
async def get_league_matches(league_name: str):
    league_name = league_name.lower()

    if league_name in LEAGUE_URLS:
        url = LEAGUE_URLS[league_name]
        matches = fetch_match_fixtures(url, league_name)
    else:
        return {"error": "Invalid league name"}

    return {"matches": matches}

