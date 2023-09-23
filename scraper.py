import requests
from bs4 import BeautifulSoup

def scrape_live_scores():
    url = "https://www.espncricinfo.com/live-cricket-score"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    team1 = soup.find("div", class_="team team1")
    team2 = soup.find("div", class_="team team2")
    summary = soup.find("div", class_="status-text")

    if team1 and team2 and summary:
        team1_name = team1.find("span", class_="name-detail").text.strip()
        team1_score = team1.find("span", class_="score-detail").text.strip()
        team2_name = team2.find("span", class_="name-detail").text.strip()
        team2_score = team2.find("span", class_="score-detail").text.strip()
        match_summary = summary.text.strip()

        return f"Team 1: {team1_name} ({team1_score})\nTeam 2: {team2_name} ({team2_score})\nSummary: {match_summary}"
    else:
        return "No live scores available! Try again later."

