from flask import Flask, render_template, request
import utils2, time

app = Flask(__name__)

@app.route('/')
def home():

    utils2.fetch_data()
    length = len(utils2.music_dir)
    return render_template('home.html', music=utils2.music_dict)


if __name__ == "__main__":
    app.run()
