from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)



@app.route('/get_chance', methods=['POST'])
def get_chance():
    data = request.data.decode("utf-8")
    data = json.loads(data)

    newlq = data["team1"]
    newlq1 = data["team2"]
    random_stadium = data["stadium"]

    probability = 100
    if newlq == 'LA Lakers' and random_stadium == 'Staples Center':
        prob = (probability - 20)   
    elif newlq1 == 'LA Lakers' and random_stadium == 'Staples Center':
        prob = (probability - 20)    
    elif newlq == 'Brooklyn Nets' and random_stadium == 'Barclays Center':
        prob = (probability - 30)    
    elif newlq1 == 'Brooklyn Nets' and random_stadium == 'Barclays Center':
        prob = (probability - 30)
    elif newlq == 'Toronto Raptors' and random_stadium == 'Scotiabank Arena':
        prob = (probability - 35)
    elif newlq1 == 'Toronto Raptors' and random_stadium == 'Scotiabank Arena':
        prob = (probability - 35)
    else:
        prob = (probability - 50)
   # return prob
    return jsonify(Probability = prob)


    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)