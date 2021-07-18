from flask import Flask, request, jsonify
import random


app = Flask(__name__)

# animal generator route here
@app.route('/get_teams')
def get_teams():
    lq = ['LA Lakers', 'Toronto Raptors', 'Brooklyn Nets']
    newlq = random.choice(lq)
    newlq1 = random.choice(lq)
    while newlq == newlq1:
        newlq1 = random.choice(lq)
    return jsonify(team1=newlq, team2=newlq1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)