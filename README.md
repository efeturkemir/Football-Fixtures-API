## ⚽ Football Fixtures API

A FastAPI-powered service to retrieve real-time match fixtures and results for the Super League (Turkey) and Premier League (England).

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
```

## 🧑💻 Usage Example
```bash
# Fetch Super League matches
curl http://localhost:8000/matches/super_league
```

### Sample Response:
```json
{
  "matches": [
    {
      "date": "14.02.2025",
      "time": "20:00",
      "home_team": "ADANA DEMİRSPOR A.Ş.",
      "away_team": "ONVO ANTALYASPOR",
      "home_goals": 1,
      "away_goals": 1,
      "league": "Super Lig"
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
- League identification
```

## 🤝 Contributing
```bash
Contributions are welcome! Please open an issue first to discuss proposed changes.
