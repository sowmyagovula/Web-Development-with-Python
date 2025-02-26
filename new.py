from flask import Flask, render_template

app = Flask(__name__)

JOBs = [
    {
        'id' : 1,
        'Position' : "Software Engineer",
        'Location' : "Bengaluru, Hyderabad",
        'Salary' : 'Rs. 12,00,000'
    },
    {
        'id' : 2,
        'Position' : "Data Scientist",
        'Location' : "Hyderabad",
        'Salary' : 'Rs. 18,00,000'
    },
    {
        'id' : 3,
        'Position' : "Python Developer",
        'Location' : "Bengaluru, Hyderabad",
        'Salary' : 'Rs. 12,00,000'
    },
    {
        'id' : 4,
        'Position' : "Fullstack Developer",
        'Location' : "Bengaluru, Chennai, Hyderabad",
        'Salary' : 'Rs. 20,00,000'
    }]

@app.route("/")
def home():
    return render_template("hpme.html", 
                           jobs=JOBs)

if __name__ == "__main__":
    app.run(port = 8080, debug = True)