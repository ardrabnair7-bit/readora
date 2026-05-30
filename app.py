from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "readora_secret_key"

# ---------------- MYSQL CONNECTION ----------------
from urllib.parse import quote_plus

# Encode password safely
password = quote_plus("9037414934@Ardra")

# MySQL connection

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://readora_user:Readora%40123@localhost/readora"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

# ---------------- DATABASE MODELS ----------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    book_title = db.Column(db.String(200))
    rating = db.Column(db.Integer)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    brief = db.Column(db.String(300))
    content = db.Column(db.Text)
    category = db.Column(db.String(50))

# ---------------- SEED DATA (ONLY 5 BOOKS) ----------------

def add_books():

    # Prevent duplicate books
    if Book.query.count() > 0:
        return

    sample_books = [

        # ---------------- CHILDREN ----------------
        Book(
            title="The Magic Tree House",
            brief="Time travel adventure for kids",
            content="Jack and Annie discover a magical treehouse.",
            category="children"
        ),

        Book(
            title="Peter Pan",
            brief="A boy who never grows up",
            content="Peter Pan takes Wendy to Neverland.",
            category="children"
        ),

        Book(
            title="Cinderella",
            brief="A magical fairy tale story",
            content="Cinderella attends the royal ball with magic.",
            category="children"
        ),

        # ---------------- NOVELS ----------------
        Book(
            title="1984",
            brief="Dystopian world under surveillance",
            content="Winston secretly rebels against Big Brother.",
            category="novels"
        ),

        Book(
            title="The Alchemist",
            brief="A journey to follow dreams",
            content="Santiago searches for treasure and purpose.",
            category="novels"
        ),

        Book(
            title="The Hobbit",
            brief="Adventure to defeat a dragon",
            content="Bilbo joins dwarves on a dangerous mission.",
            category="novels"
        ),

        # ---------------- HORROR ----------------
        Book(
            title="Dracula",
            brief="Classic vampire horror",
            content="Count Dracula spreads fear everywhere.",
            category="horror"
        ),

        Book(
            title="The Shining",
            brief="Haunted hotel horror",
            content="A hotel slowly drives Jack insane.",
            category="horror"
        ),

        Book(
            title="It",
            brief="Terrifying clown story",
            content="Children face an evil clown named Pennywise.",
            category="horror"
        ),

        # ---------------- COMEDY ----------------
        Book(
            title="Diary of a Wimpy Kid",
            brief="Funny school adventures",
            content="Greg faces funny middle school problems.",
            category="comedy"
        ),

        Book(
            title="Yes Man",
            brief="A man says yes to everything",
            content="Carl changes his life completely.",
            category="comedy"
        ),

        Book(
            title="Good Omens",
            brief="Funny angel and demon story",
            content="An angel and demon try stopping apocalypse.",
            category="comedy"
        ),

        # ---------------- STUDENT ----------------
        Book(
            title="Math Guide",
            brief="Basic mathematics learning",
            content="Learn addition, subtraction and algebra.",
            category="student"
        ),

        Book(
            title="Science Basics",
            brief="Introduction to science",
            content="Physics, chemistry and biology explained.",
            category="student"
        ),

        Book(
            title="English Grammar",
            brief="Grammar made simple",
            content="Learn nouns, verbs and sentence formation.",
            category="student"
        ),
    ]

    db.session.add_all(sample_books)
    db.session.commit()

    print("✅ 15 books added successfully")
# ---------------- ROUTES ----------------

@app.route("/")
def home():
    if "user" in session:
        categories = db.session.query(Book.category).distinct().all()
        categories = [c[0] for c in categories]
        return render_template("index.html", user=session["user"], categories=categories)
    return redirect(url_for("login"))

# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        if User.query.filter_by(username=username).first():
            return "User already exists"

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        session["user"] = username
        return redirect(url_for("home"))

    return render_template("register.html")

# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user"] = username
            return redirect(url_for("home"))

        return "Invalid credentials"

    return render_template("login.html")

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# ---------------- CATEGORY ----------------
@app.route("/category/<name>")
def category(name):
    books_list = Book.query.filter_by(category=name).all()
    return render_template("category.html", category=name, books=books_list)

# ---------------- BOOK PAGE ----------------
@app.route("/book/<int:book_id>")
def book(book_id):
    book_data = Book.query.get_or_404(book_id)

    ratings = Rating.query.filter_by(book_title=book_data.title).all()
    avg = sum([r.rating for r in ratings]) / len(ratings) if ratings else 0

    return render_template("book.html", book=book_data, avg=avg)

# ---------------- RATE BOOK ----------------
@app.route("/rate/<int:book_id>", methods=["POST"])
def rate(book_id):
    if "user" not in session:
        return redirect(url_for("login"))

    book_data = Book.query.get_or_404(book_id)
    rating_value = int(request.form["rating"])

    new_rating = Rating(
        username=session["user"],
        book_title=book_data.title,
        rating=rating_value
    )

    db.session.add(new_rating)
    db.session.commit()

    return redirect(url_for("book", book_id=book_id))

# ---------------- PROFILE ----------------
@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login"))

    user = User.query.filter_by(username=session["user"]).first()
    return render_template("profile.html", user=user)

# ---------------- RUN ----------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        add_books()

    app.run(debug=True)
