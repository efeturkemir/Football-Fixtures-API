## ⚽ Football Fixtures API

A FastAPI-powered service to retrieve real-time match fixtures and results for the Super League (Turkey), Premier League (England), Serie A (Italy), La Liga (Spain), and Bundesliga (Germany).

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/efeturkemir/football-fixtures-api)

## 🌟 Features
```bash
- Get upcoming matches for both leagues
- View completed match results
- Simple RESTful API endpoints
- Fast response times with asynchronous processing
- Clean JSON response format
```

## 🚀 Installation
```bash
# Clone the repository
git clone https://github.com/efeturkemir/football-fixtures-api.git

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

## 📌 API Endpoints
```bash
# Get Super League Matches
GET /matches/super_league

# Get Premier League Matches
GET /matches/premier_league

# Get Serie A Matches
GET /matches/serie_a

# Get La Liga Matches
GET /matches/la_liga

# Get Bundesliga Matches
GET /matches/bundesliga
```

## 🧑💻 Usage Example
```bash
# Fetch Super League matches
curl http://localhost:8000/matches/super_league

# Fetch Serie A matches
curl http://localhost:8000/matches/serie_a
```

### Sample Response:
```json
{
  "matches": [
  {
      "home_team": "Manchester United",
      "away_team": "Ipswich Town",
      "date": "26/02/2025",
      "time": "21:30",
      "home_goals": null,
      "away_goals": null
    }
  ]
}
```

## 📋 Data Structure
```bash
Each match contains:
- Date (DD.MM.YYYY format)
- Match time (HH:MM)
- Home and away team names
- Goals scored (for completed matches)
- League identification (Super Lig, Premier League, Serie A, La Liga, Bundesliga)
```

## 🤝 Contributing
```bash
Contributions are welcome! Please open an issue first to discuss proposed changes.
