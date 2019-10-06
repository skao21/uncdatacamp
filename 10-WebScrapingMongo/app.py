from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import time
import scrape_mars

# Use flask_pymongo to set up mongo connection
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")
# route
@app.route("/")
def index():
    
    mars = mongo.db.mars.find_one()
    if mars == None:
        # loading  collection mar if nothing in the data base mars_db
        mongo.db.mars.update({}, scrape_mars.scrape_all_sites(), upsert=True)
        time.sleep(1)
        mars = mongo.db.mars.find_one()
    
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    data = scrape_mars.scrape_all_sites()
    mars.update({}, data, upsert=True)
    
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
