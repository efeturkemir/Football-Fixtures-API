from fastapi import FastAPI
from app.fetch_super_league import fetch_super_league_fixtures
from app.fetch_premier_league import fetch_premier_league_fixtures

app = FastAPI()

@app.get("/matches/super_league")
async def get_super_league_matches():
    matches = fetch_super_league_fixtures()
    return {"matches": matches}

@app.get("/matches/premier_league")
async def get_premier_league_matches():
    matches = fetch_premier_league_fixtures()
    return {"matches": matches}



