# 🌤️ CLI Weather Dashboard

A modular, clean command-line interface (CLI) application built with Python. This app fetches real-time weather profiles and 5-day forecasts via the OpenWeatherMap API, parses the JSON payloads cleanly, and formats them beautifully into your terminal complete with visual emojis and smart local file caching.

---

## 📁 Project Directory Structure

Ensure your project folders and files match this tree structure in Visual Studio Code:

week6-weather-dashboard/
│── weather_app/
│   ├── __init__.py
│   ├── config.py
│   ├── weather_api.py
│   ├── weather_parser.py
│   ├── weather_display.py
│   └── main.py
│── data/
│   └── cache/
│── requirements.txt
│── .env
│── .env.example
│── .gitignore
└── README.md

---

## 🛠️ Step 1: Configuration & Environment Setup

### 1. `.gitignore`
Prevents local environment variables, temporary cache files, and Python compiled scripts from tracking into your Git repositories.
```text
.env
__pycache__/
*.pyc
data/cache/