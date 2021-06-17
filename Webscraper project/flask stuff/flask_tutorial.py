from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submissions", methods=["POST", "GET"])
def submissions():
    # if my text box on the site is filled with text, then that text is stored in the session as the 'user'. Then the url is redirected to the /user page and it's scripts. This requires POST method, so if the method is NOT POST (i.e. GET), then the page redirects to the same page again, basically asking you to do the right thing (i.e. submit text into the box).
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successfull!")
        return redirect(url_for("user"))
    else:
        # if the "user" is present in the session already, then the page will be redirected to the "user" page, displayed the "user" data as an h1 header.
        if "user" in session:
            flash("Already logged in feller!")
            return redirect(url_for("user"))

        return render_template("submissions.html")

@app.route("/user")
def user():
    # so the POST method req has been filled. Now that the user data is stored in the session, the webpage then displays that text on the screen as a h1 header. That's only if the session has "user" data stored already. In the case that there is no "user" data stored in session, the page is then redirected to the /submissions page to get the user to fill the textbox. 
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You ain logged in feller!")
        return redirect(url_for("submissions"))

# Manual clearing of session data, leaving no data up to chance. Uses '.pop' helper function to remove the "user" data from session at the given key. Since the "user" key is passed, it will "pop", or return the list without that key, to/from sessions. This updates the list enitrely instead of creating a new list without the key, better for being dynamic in this specific situation. Pop has a second argument (default), and this default is meant to be returned if the first argument, key, is absent. In this case, the default is assigned as None, so if there is no "user" key present in session, it will return None, instead of raising an exception. #Update: Don't pass None, this is bad. Raising execptions is meant to throw you clues as to why code is written with poor objectives, and in this case, it would act like a bypass to the execption because None being passed won't be seen as an actual indicator of a critical error in the code logic. 
# After "user" data is popped from session, the page is then redirected to submissions. This simulates a typical logout behavior of a webpage when you successfully logout of the webpage and it returns you to the login page.
# However, this does not handle removing data from the entire session when the session is closed out. This only removes data if I manually tell it to remove it, using "/logout" in the address bar. If I close the application, it still retains the information, which is bad. 
@app.route("/logout")
def logout():
    flash(f"You been logged out tho.", "info")
    session.pop("user", None)
    return redirect(url_for("submissions"))


if __name__ =="__main__":
    app.run(debug=True)
