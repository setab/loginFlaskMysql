from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Your MySQL username
    password="100123",  # Your MySQL password
    database="login_db",
    port=33061
)

# Route for login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            return "Login Successful!"
        else:
            return "Invalid Credentials. Please try again."

    return render_template('login.html')

@app.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        newUserName = request.form['new-username']
        newPassword = request.form['new-password']
        
        cursor = db.cursor()
        
        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (newUserName, newPassword))
        
        # Commit the transaction
        db.commit()
        
        # Check if the user was inserted successfully
        if cursor.rowcount > 0:
            return "Sign in successful"
        else:
            return "Failed to sign in"
    
    # If request method is GET, render the signin page
    return render_template('signin.html')

if __name__ == '__main__':
    app.run(debug=True)
