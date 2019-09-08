# 1. import Flask
from flask import Flask, jsonify
import numpy as np
from datetime import datetime, timedelta 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# 3. Define what to do when a user hits the index route
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route("/api/v1.0/precipitation")
def prcp_query():
    """
        Convert the query results to a Dictionary using `date` as the key and
        `prcp` as the value.
    """
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).group_by(Measurement.date).all()
    all_prcps = []
    for r in results:
        prcp_dict = {}
        prcp_dict[r[0]] = r[1]
        all_prcps.append(prcp_dict)
    return jsonify(all_prcps)

@app.route("/api/v1.0/stations")
def station_query():
    """Return a JSON list of stations from the dataset.n"""
    session = Session(engine)
    results = session.query(Station.station).all()
    all_names = list(np.ravel(results))
    return jsonify(all_names)

@app.route("/api/v1.0/tobs")
def tobs_query():
    """
        query for the dates and temperature observations from a year from the last data point.
        Return a JSON list of Temperature Observations (tobs) for the previous year.
    """
    session = Session(engine)
    st_hightest_tobs = session.query(Measurement.station,Measurement.tobs).order_by(Measurement.tobs.desc()).first()[0]

    ymde = session.query(Measurement.date, Measurement.station, Measurement.tobs). \
        filter(Measurement.station==st_hightest_tobs).order_by(Measurement.date.desc()).first()[0]

    ymds = str(datetime.strptime(ymde + ' 0:0:0.0', '%Y-%m-%d  %H:%M:%S.%f') - timedelta(days=365)).split()[0]

    results = session.query(Measurement.tobs, func.count(Measurement.tobs) ).filter(Measurement.station==st_hightest_tobs). \
                   filter(Measurement.date.between(ymds, ymde)).group_by(Measurement.tobs).all()
    
    all_temps = []
    for t in results:
        temp_dict = {}
        temp_dict[t[0]] = t[1]
        all_temps.append(temp_dict)
    return jsonify(all_temps)

def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session = Session(engine)
    print("start_d", start_date, "   end_d=", end_date)
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

@app.route('/api/v1.0/<start_d>')
def temp_attr_query(start_d):
    return  jsonify(calc_temps(start_d,"2017-08-23"))

@app.route('/api/v1.0/<start_d>/<end_d>')
def temp_attr_querys(start_d, end_d):   
    return   jsonify(calc_temps(start_d,end_d))

if __name__ == "__main__":
    app.run(debug=True)
