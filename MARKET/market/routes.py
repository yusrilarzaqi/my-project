from market import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    price = dict(zip([i.name for i in items], [i for i in items]))
    return render_template("market.html", items=items, price=price)


@app.route("/register", methods=['POST', 'GET'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():

        user_to_create = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password1.data,
        )
        db.session.add(user_to_create)
        db.session.commit()


        return redirect(url_for("market_page"))

    # if there are not error form the falidation
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f'There was an Error with creating user: {error_msg} ')


    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login_page():
    return render_template('login.html')













