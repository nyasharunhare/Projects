import os
import io

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import requests
from google.cloud import vision
import base64



from helpers import apology, login_required

# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///date.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Get form data
        # Username
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("must enter username", 400)
        if not password:
            return apology("must enter password", 400)

        if password != confirmation:
            return apology("Password and Confirm password does not match")

        # If username already exists
        existing_user = db.execute("SELECT * FROM users WHERE username = :username", username=username)
        if existing_user:
            return apology("username already exists", 400)

        # Password
        password = request.form.get("password")
        if not password:
            return apology("must enter password", 400)

        # Confirmation
        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("must enter confirmation", 400)

        if confirmation != password:
            return apology("passwords do not match", 400)

        # hash password
        hash= generate_password_hash(password)

        # Insert new user into users table
        try:
            result = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            new_user_id = db.execute("SELECT id FROM users WHERE username = ?", username)[0]['id']
            # Remember which user has logged in
            session["user_id"] = new_user_id
        except Exception as e:
            print(e)
            return apology("registration failed", 400)

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/reset", methods=["GET", "POST"])
@login_required
def reset():
    """Reset Password"""
    if request.method == "POST":
        # Get input from form
        old_password = request.form.get("old_password").upper()
        new_password = request.form.get("new_password").upper()

        # Fetch current user's password hash
        user = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
        # Compare old password with stored hash
        if not check_password_hash(user[0]["hash"], old_password):
            return apology("error: wrong old password", 400)
        # Hash the new password
        new_password_hash = generate_password_hash(new_password)
        # Update the user's password in the database
        try:
            db.execute("UPDATE users SET hash = :hash WHERE id = :id", hash=new_password_hash, id=session["user_id"])
        except Exception as e:
            print(e)
            return apology("error resetting password", 400)

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("reset.html")


# Set up your Google Cloud Vision API details
api_key = 'AIzaSyBBeDpLerIuzTG7m86WwkWMf8L9ZWdQMFw'
url = "https://vision.googleapis.com/v1/images:annotate"

# Mapping of emotions to emojis
# Expanded mapping of emotions to emojis with different reactions
emotion_to_emoji = {
    "VERY_LIKELY": "😁",  # Grinning face for very likely joy
    "LIKELY": "😊",       # Smiling face for likely joy
    "POSSIBLE": "🙂",      # Slightly smiling face for possible joy
    "UNLIKELY": "😐",     # Neutral face for unlikely joy
    "VERY_UNLIKELY": "😦",  # Frowning face for very unlikely joy
}

# Weights for scoring the emojis
emoji_weights = {
    "😁": 3,   # High positive score for grinning
    "😊": 2,   # Positive score for smiling
    "🙂": 1,   # Slightly positive score for slight smile
    "😐": 0,   # Neutral score
    "😦": -1   # Slight negative score for frown
}

# Store received emojis for scoring
received_emojis = []

def detect_emotion(image_content):
    image_base64 = base64.b64encode(image_content).decode('utf-8')
    payload = {
        "requests": [{
            "image": {"content": image_base64},
            "features": [{"type": "FACE_DETECTION"}]
        }]
    }
    headers = {'Content-Type': 'application/json'}
    params = {'key': api_key}
    response = requests.post(url, headers=headers, json=payload, params=params)
    annotations = response.json().get('responses', [{}])[0].get('faceAnnotations', [])

    if annotations:
        face = annotations[0]
        joy_likelihood = face.get('joyLikelihood', 'VERY_UNLIKELY')
        return emotion_to_emoji[joy_likelihood]
    return '😐'

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image_content = image_file.read()
    emoji = detect_emotion(image_content)
    received_emojis.append(emoji)  # Append the detected emoji
    return jsonify({'emoji': emoji})

@app.route('/get_feedback', methods=['GET'])
def get_feedback():
    total_score = sum(emoji_weights.get(emoji, 0) for emoji in received_emojis)  # Calculate total score based on weights

    if total_score > 10:
        feedback = "Guess your crush has a soft spot for you too. All that smiling and blushing for you!"
    elif total_score > 0:
        feedback = "Caught your crush smiling here and there, guess you have a shot buddy."
    else:
        feedback = "Your crush is a tough one to impress, better luck next time!"

    return jsonify({'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True)
