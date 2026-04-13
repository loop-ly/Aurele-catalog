from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

def load_products():
    if os.path.exists("catalog.json"):
        with open("catalog.json", "r") as file:
          return json.load(file)
    return[]
@app.route("/")
def home():
    products = load_products()
    return render_template("home.html", products=products)

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route("/add", methods =["POST"])
def add():
   product = request.form["product"]
   products = load_products()
   products.append(product)
   with open("catalog.json", "w") as file:
       json.dump(products, file)
   return redirect("/")

@app.route("/remove", methods=["POST"])
def remove():
   product = request.form["product"]
   products = load_products()
   products.remove(product)
   with open("catalog.json", "w") as file:
      json.dump(products, file)
   return redirect("/")
   
@app.route("/search", methods=["POST"])
def search():
   query = request.form["query"]
   products = load_products()
   results = [p for p in products if query.lower() in p.lower()]
   return render_template("home.html", products = results)


if __name__== "__main__":
   app.run(debug=True)    
