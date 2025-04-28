from flask import Flask, render_template, request
import music  # Assuming you have a music.py file handling recommendations
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # or your main HTML

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form['user_input']
    recommendations = music.get_recommendations(user_input)
    return render_template('results.html', recommendations=recommendations)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # Get PORT from Railway
    app.run(host="0.0.0.0", port=port)  # Listen on all interfaces
