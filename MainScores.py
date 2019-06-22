from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def score_server():
    content = open("scores.txt", 'r')
    score = content.read()
    content.close()
    try:
        return render_template('Score.html', SCORE=score)
    except FileNotFoundError as error:
        return render_template('Error.html', ERROR=error)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


