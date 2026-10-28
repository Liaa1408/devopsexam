from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        student_id = request.form["student_id"]
        email = request.form["email"]

        return render_template("success.html", name=name)

    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)