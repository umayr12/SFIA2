from flask import Flask, request, jsonify
import random
import json

app = Flask(__name__)



# animal noise generator route here
@app.route('/get_stadium')
def get_stadium():
    stadium = ['Staples Center', 'Barclays Center', 'Scotiabank Arena']
    random_stadium = random.choice(stadium)
    return jsonify(stadium=random_stadium)

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)