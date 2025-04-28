from flask import Flask, render_template, request
from music import search_song

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    songs = []
    if request.method == 'POST':
        song_name = request.form['song']
        songs = search_song(song_name)
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
