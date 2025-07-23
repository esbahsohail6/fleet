# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import datetime

# app = Flask(__name__)
# CORS(app)

# # --- Simulated Data Stores ---
# vehicles = {
#     "vehicle_1": {"lat": 24.8607, "lng": 67.0011},
#     "vehicle_2": {"lat": 24.8611, "lng": 67.0099}
# }

# hazards = [
#     {"id": 1, "type": "Pothole", "lat": 24.8612, "lng": 67.0025, "severity": "Moderate", "timestamp": "2025-07-23T12:00:00"},
#     {"id": 2, "type": "Blockage", "lat": 24.8603, "lng": 67.0041, "severity": "High", "timestamp": "2025-07-23T12:05:00"}
# ]

# # --- Endpoints ---
# @app.route('/vehicles', methods=['GET'])
# def get_vehicles():
#     return jsonify(vehicles)

# @app.route('/hazards', methods=['GET'])
# def get_hazards():
#     return jsonify(hazards)

# @app.route('/update_location/<vehicle_id>', methods=['POST'])
# def update_location(vehicle_id):
#     data = request.json
#     vehicles[vehicle_id] = {"lat": data['lat'], "lng": data['lng']}
#     return jsonify({"status": "updated", "vehicle": vehicle_id})

# @app.route('/add_hazard', methods=['POST'])
# def add_hazard():
#     data = request.json
#     new_hazard = {
#         "id": len(hazards) + 1,
#         "type": data.get("type", "Unknown"),
#         "lat": data["lat"],
#         "lng": data["lng"],
#         "severity": data.get("severity", "Low"),
#         "timestamp": datetime.datetime.now().isoformat()
#     }
#     hazards.append(new_hazard)
#     return jsonify({"status": "hazard added", "hazard": new_hazard})

# if __name__ == '__main__':
#     app.run(debug=True)





from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# --- Simulated Data Stores ---
vehicles = {
    "vehicle_1": {"lat": 24.8607, "lng": 67.0011},
    "vehicle_2": {"lat": 24.8611, "lng": 67.0099}
}

hazards = [
    {"id": 1, "type": "Pothole", "lat": 24.8612, "lng": 67.0025, "severity": "Moderate", "timestamp": "2025-07-23T12:00:00"},
    {"id": 2, "type": "Blockage", "lat": 24.8603, "lng": 67.0041, "severity": "High", "timestamp": "2025-07-23T12:05:00"}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify(vehicles)

@app.route('/hazards', methods=['GET'])
def get_hazards():
    return jsonify(hazards)

@app.route('/update_location/<vehicle_id>', methods=['POST'])
def update_location(vehicle_id):
    data = request.json
    vehicles[vehicle_id] = {"lat": data['lat'], "lng": data['lng']}
    return jsonify({"status": "updated", "vehicle": vehicle_id})

@app.route('/add_hazard', methods=['POST'])
def add_hazard():
    data = request.json
    new_hazard = {
        "id": len(hazards) + 1,
        "type": data.get("type", "Unknown"),
        "lat": data["lat"],
        "lng": data["lng"],
        "severity": data.get("severity", "Low"),
        "timestamp": datetime.datetime.now().isoformat()
    }
    hazards.append(new_hazard)
    return jsonify({"status": "hazard added", "hazard": new_hazard})

if __name__ == '__main__':
    app.run(debug=True)
