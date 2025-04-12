from flask import Flask, render_template
from config import Config
from models import db, Student

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    students = Student.query.all()
    return render_template('dashboard.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
