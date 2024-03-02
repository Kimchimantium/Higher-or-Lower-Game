from flask import Flask
from random import randint, choice
import time

app = Flask(__name__)

rand_num = randint(0, 10)

@app.route('/')
def higher_lower():
    time.sleep(1)
    return f"<h1 style='text-align:center; color: brown'>pick a number between 0, 9</h1>"


@app.route('/<int:guess>')
def change_num(guess):
    if guess == rand_num:
        return "<h2 style='text-align:center;'>correct you've got it right</h2>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    else:
        if guess > rand_num:
            return "<h2 style='text-align:center;'>Smaller number!t</h2>" \
                    "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        else:
            return "<h2 style='text-align:center;'>Bigger number!t</h2>" \
                   "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True, port=8080)

