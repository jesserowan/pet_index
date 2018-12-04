from flask import Flask, redirect, request, render_template, session
from mysqlconnection_copy import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    mysql = connectToMySQL('c_r_pets')
    pets = mysql.query_db('SELECT * FROM pets;')
    return render_template('index.html', pets=pets)

@app.route('/add_pet', methods=["POST"])
def add_pet():
    mysql = connectToMySQL('c_r_pets')

    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(n)s, %(t)s, NOW(), NOW());"

    data = {
        "n": request.form["pet_name"],
        "t": request.form['species']
    }

    new_pet_id = mysql.query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)