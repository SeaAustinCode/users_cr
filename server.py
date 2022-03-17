from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "aab83683-64d0-4888-a2a1-ec678c92ca4d"

from model_users import User

@app.route('/')
def index():
    return redirect('/all_users')

@app.route('/all_users')
def users():
    return render_template("all_users.html", users=User.get_all())

@app.route('/process_user', methods=['post'])
def process():
    print(request.form)
    User.save(request.form)
    return redirect("/all_users")

@app.route('/create_user')
def create():
    return render_template("create_user.html")
# KEEP THIS AT THE BOTTOM 
if __name__=="__main__":
    app.run(debug=True)