from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

tank = []
id = 0
global user_object
user_object = {}
global data_object 
data_object = {}

#CREATE
@app.route("/profile", methods=["POST"])
def post():
    user_object = {
    "last_updated":datetime.datetime.now(),
    "username": request.json["username"],
    "role": request.json["role"],
    "favcolour": request.json["favcolour"]
     }
    return user_object

#READ
@app.route("/profile", methods = ["GET"])
def getuser():
    return user_object

#UPDATE
@app.route("/profile", methods = ["PATCH"])
def patchuser():
    if "username" in request.json:
        user_object["username"] = request.json["username"]
        last_updated = datetime.datetime.now()
    if "fav_color" in request.json:
        user_object["favcolour"] = request.json["favcolour"]
        last_updated = datetime.datetime.now()
    if "role" in request.json:
        user_object["role"] = request.json["role"]
        last_updated = datetime.datetime.now()        
    return user_object

#CREATE
@app.route("/data", methods=["POST"])
def post_d():
    global id
    id+=1
    data_object = {
    "location": request.json["location"],
    "full": request.json["full"],
    "lat": request.json["lat"],
    "long": request.json["long"],
    "tank_id":id
    }
    tank.append(data_object)
    return jsonify(data_object)

#READ
@app.route("/data",methods = ["GET"])
def get_data():
    return jsonify(tank)

#UPDATE
@app.route("/data/<int:id>", methods = ["PATCH"])
def patch_data(id):
    for i in tank:
        if i["tank_id"]==id:
            if "location" in request.json:
                i["location"] = request.json["location"]
                last_updated = datetime.datetime.now()
            if "full" in request.json:
                i["full"] = request.json["full"]
                data_updated = datetime.datetime.now()
            if "lat" in request.json:
                i["lat"] = request.json["lat"]
                last_updated = datetime.datetime.now() 
            if "long" in request.json:
                i["long"] = request.json["long"]
                last_updated = datetime.datetime.now()           
    return jsonify(tank)

#DELETE 
@app.route("/data/<int:id>", methods = ["DELETE"])
def delete(id):
    for location in tank:
        if location["tank_id"] == id:
            tank.remove(location)
    return {
        "success":True
    }


if __name__ == "__main__":
    app.run(debug = True, port = 3000, host = "0.0.0.0")