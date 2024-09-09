from flask import Flask,render_template,url_for
from emp import employees_data
app=Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")

@app.route("/about")
def about():
    return render_template("about.html",title="About")
@app.route("/emp")
def emp():
    return render_template(
        "emp.html",
        title="employees",
        employees=employees_data
    )
@app.route("/emp/manager")
def manager():
    return render_template(
        "manager.html",
        title="Manager",
        employees=employees_data
    )
if __name__=="__main__":
    app.run(debug=True)