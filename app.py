
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")



# analyze number  

@app.route("/api/analyze", methods=["POST"])
def analyze_number():

    data = request.get_json()

    number=int(data["number"])

    # Even / Odd
    even = number % 2 == 0
    odd = not even

    # Positive / Negative / Zero
    positive = number > 0
    negative = number < 0
    zero = number == 0

    # Prime
    if number < 2:
        prime = False
    else:
        prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break

    # Palindrome
    number_string = str(abs(number))
    palindrome = number_string == number_string[::-1]

    # Armstrong
    digits = number_string
    power = len(digits)

    armstrong_sum = sum(
        int(digit) ** power
        for digit in digits
    )

    armstrong = armstrong_sum == abs(number)


    # Send result back to HTML
    return jsonify({
        "number": number,
        "even": even,
        "odd": odd,
        "positive": positive,
        "negative": negative,
        "zero": zero,
        "prime": prime,
        "palindrome": palindrome,
        "armstrong": armstrong
    })




if __name__ == "__main__":
    app.run(debug=True)



