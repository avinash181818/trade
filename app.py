from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='Avinash', password='Shivanna'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

    return render_template('login.html')
# Breathing page
@app.route('/breathing1')
def breathing1():
 return render_template('breathing.html')

# Feedback page
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/trade')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('trade.html')
@app.route('/logout')
def logout():
     session.pop('user_id',None)
     return render_template('login.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,  debug=True)
