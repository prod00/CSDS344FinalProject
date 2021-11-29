from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def login_page():
    if request.method == "POST":
        password = request.form.get("pword")
        if password == "apple":
            return redirect(url_for('top_secret_page'))
    return render_template('index.html')

@app.route('/secret_page')
def top_secret_page():
    return render_template('succesful_login.html')



if __name__ == '__main__':
    app.run()
