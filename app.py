from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

DATABASE = []
tank = []
tankid = 0
global user_object
user_object = ("","","","")

#CREATE
@app.route("/profile", methods=["POST"])
def post():
    user = request.json["username"]
    fav_colour = request.json["favcolour"]
    r = request.json["role"]
    time = datetime.datetime.now()
    user_object = {
    "last_updated":time,
    "username": user,
    "favcolour": fav_colour,
    "role": r
     }
    DATABASE.append(user_object)
    return user_object

#READ
@app.route("/profile", methods = ["GET"])
def getuser():
    return jsonify(DATABASE)

#UPDATE
@app.route("/profile", methods = ["PATCH"])
def patchuser():
    if "username" in request.json:
        user["username"] = request.json["username"]
        last_updated = datetime.datetime.now()
    if "fav_color" in request.json:
        fav_colour["favcolour"] = request.json["favcolour"]
        last_updated = datetime.datetime.now()
    if "role" in request.json:
        r["role"] = request.json["role"]
        last_updated = datetime.datetime.now()        
    return jsonify(DATABASE)

#CREATE
@app.route("/data", methods=["POST"])
def post_d():
    location = request.json["location"]
    full = request.json["full"]
    lat = request.json["lat"]
    long = request.json["long"]
    global tankid
    tankid +=1
    data_object = {
    "tank_id":tankid,
    "location":location,
    "full":full,
    "lat":lat,
    "long":long
     }
    tank.append(data_object)
    return data_object

#READ
@app.route("/data",methods = ["GET"])
def get_data():
    return jsonify(tank)

#UPDATE
@app.route("/data/<int:id>", methods = ["PATCH"])
def patch_data(tankid):
    for location in tank:
        if location["tank_id"]== tankid:
            location["location"] = request.json("location")
    for full in tank:
        if full["tank_id"]==tankid:
            full["full"] = request.json("full")
    for lat in tank:
        if lat["tank_id"]==tankid:
            lat["lat"] = request.json("lat")
    for long in tank:
        if long["tank_id"]==tankid:
            long["long"] = request.json("long")

    return jsonify(tank)

#DELETE 
@app.route("/data/<int:id>", methods = ["DELETE"])
def delete(id):
    for location in tank:
        if location["tank_id"] == tankid:
            tank.remove(location)
    return f"Success"


if __name__ == "__main__":
    app.run(debug = True, port = 3000, host = "0.0.0.0")