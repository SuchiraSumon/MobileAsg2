import sqlite3
from flask import Flask, render_template, request, redirect, url_for
#from flask_ngrok import run_with_ngrok

import sys
sys.path.append('C:/Users/Asus/Desktop/A231/Mobile Web Programming/Mobile Asg 2')

from hobby_model import HobbyModel
#from person_model import Person

# Connect to SQLite database
db_path = 'C:/Users/Asus/Desktop/A231/Mobile Web Programming/Mobile Asg 2/mydatabase.db'

templates_folder = 'C:/Users/Asus/Desktop/A231/Mobile Web Programming/Mobile Asg 2/templates'
static_folder = 'C:/Users/Asus/Desktop/A231/Mobile Web Programming/Mobile Asg 2/static'

app = Flask(__name__, template_folder=templates_folder, static_folder=static_folder)
#run_with_ngrok(app)

# Function to get a connection and cursor
def get_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor

# Function to close the connection
def close_db(conn):
    conn.close()

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/main-page")
def mainpage():
    return render_template("main-page.html")

@app.route("/hobby")
def hobby():
    students = HobbyModel.get_students()
    return render_template('hobby.html', students=students)

@app.route('/hobby/<int:student_id>')
def show_hobby(student_id):
    student = HobbyModel.get_student(student_id)

    if student:
        return render_template('hobby.html', students=[student])  # Wrap the student in a list
    else:
        return render_template('hobby.html', students=[])  # Render an empty list if student is not found

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle contact form submission here
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Insert form data into the SQLite database
        insert_query = '''
        INSERT INTO form_submissions (name, email, subject, message)
        VALUES (?, ?, ?, ?)
        '''
        form_data = (name, email, subject, message)

        # Get connection and cursor
        conn, cursor = get_db()

        # Execute the query
        cursor.execute(insert_query, form_data)

        # Commit the changes and close the connection
        conn.commit()
        close_db(conn)

        # Redirect to a thank you page
        return redirect(url_for('thank_you'))

    return render_template("contact.html")

@app.route("/thank-you")
def thank_you():
    return render_template("thank-you.html")

@app.route("/view-data")
def view_data():
    # Retrieve data from the SQLite database
    select_query = '''
    SELECT name, email, subject, message
    FROM form_submissions
    '''

    # Get connection and cursor
    conn, cursor = get_db()

    # Execute the query
    cursor.execute(select_query)

    # Fetch all records
    data = cursor.fetchall()

    # Close the connection
    close_db(conn)

    # Render a template to display the data
    return render_template("view-data.html", data=data)

if __name__ == '__main__':
    app.run()