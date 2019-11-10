from flask import Flask, render_template, request
import tweepy

app = Flask(__name__)

@app.route("/")
def home():
        return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    x = 0
    try:
        if request.method == 'POST':
            try:
                userPublic = request.form['userPublic']
                userSecret = request.form['userSecret']
                accessPublic = request.form['accessPublic']
                accessSecret = request.form['accessSecret']
                try:
                    toggle = request.form['toggle']
                except:
                    x = 0
                else:
                    x = 1

            except:
                 return render_template("index.html", text="Unable to connect to your Twitter account or app.")
            else:
                # Connect to Twitter
                auth = tweepy.OAuthHandler(userPublic, userSecret)
                auth.set_access_token(accessPublic, accessSecret)
                api = tweepy.API(auth)
                try:
                    api.verify_credentials()
                    print("Authentication OK")
                    print(api.me().screen_name)
                except:
                    print("Error during authentication")
                    return render_template("index.html", text="Unable to connect to your Twitter account or app.")
                else:
                    if x == 1:
                        return render_template("index.html", text="Logged in as "+api.me().name+" ("+api.me().screen_name+")")
                    else:
                        try:
                            msg = request.form['msg']
                            api.update_status(msg)
                        finally:
                             return render_template("index.html", text="Unable to connect to your Twitter account or app.")



        else:
            return render_template("index.html", text="Unable to connect to your Twitter account or app.")
    except:
        return render_template("index.html", text="Unable to connect to your Twitter account or app.")


if __name__ == "__main__":
    app.run(debug=True)
