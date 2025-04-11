from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        mass = float(request.form['mass'])
        error = float(request.form['error'])
        accretion = request.form['accretion']

        if mass < 100:
            bh_type = "Stellar Black Hole"
        elif 1e5 < mass < 1e9:
            bh_type = "Supermassive Black Hole"
        elif mass >= 1e9:
            bh_type = "Ultramassive Black Hole"
        else:
            bh_type = "Intermediate Black Hole"

        result = {
            'mass': mass,
            'error': error,
            'accretion': accretion,
            'type': bh_type
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
