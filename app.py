from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
# tell sqlalchemy where the sql database is
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# sqlalchemy will manage the schema in the code
db = SQLAlchemy(app)

class Diary(db.Model):
    day = db.Column(db.Date, primary_key=True)
    entry = db.Column(db.String)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        d = Diary(day=date.today(), entry=request.form["entry"])
        db.session.add(d)
        db.session.commit()
    return render_template('today.html')



if __name__ == "__main__":
    app.run()