from flask import Flask, render_template, request
from password_generator import generate_password
from password_checker import check_strength

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    generated_password = None
    rating = None
    feedback = None

    if request.method == "POST":
        if "generate" in request.form:
            length = int(request.form.get("length", 12))
            generated_password = generate_password(length)
        
        elif "check" in request.form:
            password = request.form.get("password")
            rating, feedback = check_strength(password)

    return render_template("index.html",
                           generated_password=generated_password,
                           rating=rating,
                           feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
