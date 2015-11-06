from flask import Flask, render_template
app = Flask(__name__)

#@app.route("/presentation")
#def stuff():
#    return render_template('an_exercise_in_probability.html')

@app.route("/")
def main_page():
    return render_template('about.html')

@app.route("/Board")
def board_page():
	return render_template('board.html')

@app.route("/Contact")
def contact_page():
	return render_template('contact.html')

@app.route("/Calendar")
def calender_page():
	return render_template('calendar.html')

if __name__ == "__main__":
    #app.run(debug=True)
    app.run()