from flask import Flask, render_template
from sqlalchemy import create_engine

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/income")
def income():
    engine = create_engine(f"sqlite:///resources/sqlite/income.sqlite")
    data = engine.execute("SELECT * FROM income")
    column2 = 'Median Income'
    all_data = data.fetchall()
    print(all_data)
    return render_template("income.html", data=data, column2 = column2)

@app.route("/employment")
def employment():
    engine = create_engine(f"sqlite:///resources/sqlite/unemployment.sqlite")
    data = engine.execute("SELECT * FROM unemployment")
    return render_template("employment.html", data=data)
    


@app.route("/population")
def population():
    engine = create_engine(f"sqlite:///resources/sqlite/population.sqlite")
    data = engine.execute("SELECT * FROM population")
    column2 = 'Total Population'
    return render_template("income.html", data=data, column2=column2)

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

if __name__ == "__main__":
    app.run(debug=True)