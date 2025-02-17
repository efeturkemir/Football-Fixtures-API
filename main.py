from fastapi import FastAPI
from app.fetch_super_league import fetch_super_league_fixtures
from app.fetch_premier_league import fetch_premier_league_fixtures
from app.fetch_bundesliga import fetch_bundesliga_fixtures
from app.fetch_laliga import fetch_laliga_fixtures
from app.fetch_seriea import fetch_seriea_fixtures

app = FastAPI()

@app.get("/matches/super_league")
async def get_super_league_matches():
    matches = fetch_super_league_fixtures()
    return {"matches": matches}

@app.get("/matches/premier_league")
async def get_premier_league_matches():
    matches = fetch_premier_league_fixtures()
    return {"matches": matches}

@app.get("/matches/bundesliga")
async def get_bundesliga_matches():
    matches = fetch_bundesliga_fixtures()
    return {"matches": matches}

@app.get("/matches/la_liga")
async def get_laliga_matches():
    matches = fetch_laliga_fixtures()
    return {"matches": matches}

@app.get("/matches/serie_a")
async def get_seriea_matches():
    matches = fetch_seriea_fixtures()
    return {"matches": matches}


