from bs4 import BeautifulSoup
import requests

# User Input
sport = input("Which sport would you like to choose? ('nhl','nba','mlb','epl') ")
date = input("Which date are the matches taking place? (Year-Month-Day, Ex. 2020-01-20) ")

# Source Setup
source = requests.get('https://www.thescore.com/' + sport + '/events/date/' + date).text
soup = BeautifulSoup(source, 'lxml')

# File Setup
filename = "NHLScore.csv"
f = open(filename, "w")

FileHeaders = "Teams, Score, Time\n"
f.write(FileHeaders)

# Grabs each score
containers = soup.findAll("div",{"class":"col-xs-12 col-md-6"})
container = containers[0]

# Grabs the teams, scores, and time
teams = container.findAll("div",{"class":"EventCard__teamName--JweK5"})
scores = container.findAll("div",{"class":"EventCard__scoreColumn--2JZbq"})
time = container.findAll("div",{"class":"EventCard__clockColumn--3lEPz"})

# For loop runs through all team matchups
for container in containers:
    teams = container.findAll("div",{"class":"EventCard__teamName--JweK5"})
    team_one = teams[0].text
    team_two = teams[1].text

    scores = container.findAll("div",{"class":"EventCard__scoreColumn--2JZbq"})
    score_one = scores[0].text
    score_two = scores[1].text

    time = container.findAll("div",{"class":"EventCard__clockColumn--3lEPz"})
    time_game = time[0].text

    f.write(team_one + "," + score_one + "," + time_game + "\n")
    f.write(team_two + "," + score_two + "\n\n")

# Closes the file
f.close()
