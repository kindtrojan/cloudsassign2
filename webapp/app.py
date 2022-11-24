from flask import Flask
import integral

from markupsafe import escape

app = Flask(__name__)


@app.route('/integral/<lower>/<upper>')
def show_user_profile(lower, upper):
    # show the user profile for that user
    print("Hello")
    result = integral.looper(float(lower), float(upper))
    return f'User {result}'
