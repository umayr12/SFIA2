from flask import Flask, render_template, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import json
from sqlalchemy import desc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:basketball@34.142.65.116:3306/plate'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Basketball(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_One = db.Column(db.String(200))
    team_Two = db.Column(db.String(200))
    stadium_One = db.Column(db.String(200))
    chance_One = db.Column(db.Integer)
db.create_all()

@app.route('/')
def home():
    teams = json.loads(requests.get('http://teams_api:5001/get_teams').text)

    
    team1 = teams["team1"]
    team2 = teams["team2"]

    stadium = json.loads(requests.get('http://stadium_api:5002/get_stadium').text)
    stadium = stadium["stadium"]
    


    data = {"team1":team1, "team2":team2, "stadium":stadium}
    chance = requests.post('http://chance_api:5003/get_chance',json=data).text

    chance = json.loads(chance)
 
    chance = chance["Probability"]
    
    if chance == 80:
        j = 'LA Lakers have the home advantage with a 80 Percent chance of winning'
    elif chance == 70:
        j = 'Brooklyn Nets have the home advantage with a 70 Percent chance of winning'
    elif chance== 65:
        j = 'Toronto Raptors have the home advantage with a 65 Percent chance of winning'
    else:
        j = 'No team has a home advantage and there is a 50 Percent chance of winning for each team'
        

    


    last_five_games = Basketball.query.order_by(desc(Basketball.id)).limit(4).all()
    
    db.session.add(
    Basketball(
        team_One = team1,
        team_Two = team2, 
        stadium_One = stadium,
        chance_One = chance,
        )
    )
    db.session.commit()
    return render_template('index.html', team1=team1, team2=team2, stadium=stadium, chance=chance, j=j, all=last_five_games)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)