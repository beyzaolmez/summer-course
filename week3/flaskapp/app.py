from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    # Show the input form
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    # Read the submitted values and validate them
    weight_raw = request.form.get("weight", "")
    height_raw = request.form.get("height", "")

    try:
        weight = float(weight_raw)
        height = float(height_raw)
    except ValueError:
        return render_template("index.html", error="Please enter numbers only.")

    if weight <= 0 or height <= 0:
        return render_template("index.html", error="Values must be greater than zero.")

    # Process the input: height is given in centimetres
    metres = height / 100
    bmi = weight / (metres * metres)

    return render_template(
        "result.html",
        bmi=round(bmi, 1),
        category=categorise(bmi),
    )


def categorise(bmi):
    # Standard WHO BMI categories
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    app.run(debug=True)
