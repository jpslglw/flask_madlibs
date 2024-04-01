from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__) # server creation
app.config['SECRET_KEY'] = "secret" # configuring key
app.debug = True

debug = DebugToolbarExtension(app)

@app.route('/') # @ is decorator
def generate_form():
    """Show form for input words"""

    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story') # @ is decorator
def show_story():
    """Create story and display in html"""

    text = story.generate(request.args)
    return render_template('story.html', text=text)