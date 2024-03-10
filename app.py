from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='docs', static_folder='docs/static')
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Dummy user credentials for demonstration purposes
users = {'username': 'password'}

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('select_smiski'))
        else:
            error = 'Invalid credentials. Please try again.'
    return render_template('index.html', error=error)

@app.route('/select_smiski')
def select_smiski():
    return render_template('select_smiski.html')

@app.route('/selected')
def selected():
    series = request.args.get('series')
    return render_template('selected.html', series=series)

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__, template_folder='docs', static_folder='docs/static')


# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/series_selection', methods=['POST'])
# def series_selection():
#     # Add your login logic here (e.g., check credentials)
#     username = request.form.get('username')
#     password = request.form.get('password')

#     # Example: Check if the username and password are correct
#     if username == 'admin' and password == 'admin':
#         # Redirect to the main page with a session variable indicating login
#         return render_template('select_smiski.html', username=username)

#     else:
#         # Redirect back to the login page with an error message
#         return redirect(url_for('index', error='Invalid credentials'))

# @app.route('/main_page')
# def main_page():
#     # Access the username from the session
#     username = request.args.get('username')
#     return render_template('select_smiski.html', username=username)  # Render your main page

# @app.route('/selected/')
# def selected():
#     # Access the series parameter from the query string
#     series = request.args.get('series')
#     return render_template('selected.html', series=series)

# if __name__ == '__main__':
#     app.run(debug=True)  

