from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "693716afcff6affecebc28906a78f3ef"

posts = [
    {
        "author": "donghyeon",
        "title": "Some Random Post",
        "content": "I want to go home",
        "date_posted": "2020-01-01"
    },
    {
        "author": "Jo Yuri",
        "title": "Some Random Post 2",
        "content": "I want to go home",
        "date_posted": "2020-01-02"
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("account created")
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@root.com' and form.password.data == 'admin':
            flash(f"You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash(f"Login Unsuccessful. Fuck You!", 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
