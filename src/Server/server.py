from flask import Flask, request, render_template
from PythonFiles.returnVote import votePercent
from PythonFiles.findLocation import getLocation
from PythonFiles.addVote import addVote
from PythonFiles.createVote import createVote

app = Flask(__name__)

@app.route('/')
def index():
    # Render the form from the separate HTML file
    return render_template('index.html')

@app.route('/score')
def score():
    try:
        result = votePercent()
        result = result * 100
        # Render the result in a separate HTML file using a template variable
        return render_template('result.html', result=result)
    except Exception as e:
        return f"<h2>Error: {str(e)}</h2>", 400

@app.route('/vote')
def vote():
    # Retrieve the vote value from the form submission.
    return render_template('vote.html')

@app.route('/voted', methods=['POST'])
def voted():
    #Collecting Values
    vote_value = int(request.form.get('vote'))
    location = request.form.get('location')
    try:
        lat, lon = getLocation(location)
        addVote(vote_value, lat, lon) #Adds to database
    except Exception as e:
        return f"<h2>Error: Vote Failure</h2>", 400

    # This renders a simple page thanking the user.
    return render_template('voted.html')

@app.route('/create')
def create():
    # Retrieve the vote value from the form submission.
    return render_template('create.html')

@app.route('/created', methods=['POST'])
def created():
    #Collecting Values
    name = request.form.get('name')
    
    createVote(name) #Creates vote with name
    # This renders a simple page thanking the user.
    return render_template('voted.html')

if __name__ == '__main__':
    app.run(debug=True)
