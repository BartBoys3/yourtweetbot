from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/submit')
def background_process_test():
    print "Hello"
    return "nothing"

if __name__ == "__main__":
    app.run(debug=True)
