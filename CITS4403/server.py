from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder='static')


# 用于存储车辆位置的全局变量
vehicle_data = []
traffic_lights_positions = []
circle_positions = []

@app.route('/update_positions', methods=['POST'])
def update_positions():
    global vehicle_data
    vehicle_data = request.json
    return "Vehicle data updated", 200

@app.route('/update_traffic_lights', methods=['POST'])
def update_traffic_lights():
    global traffic_lights_positions
    traffic_lights_positions = request.json
    return "Traffic lights positions updated", 200

@app.route('/update_circle_positions', methods=['POST'])
def update_circle_positions():
    global circle_positions
    circle_positions = request.json
    return "Circle positions updated", 200

@app.route('/get_positions', methods=['GET'])
def get_vehicle_positions():
    global vehicle_data
    response = jsonify(vehicle_data)
    return response

@app.route('/get_traffic_lights', methods=['GET'])
def get_traffic_lights():
    global traffic_lights_positions
    response = jsonify(traffic_lights_positions)
    return response

@app.route('/get_circle_positions', methods=['GET'])
def get_circle_positions():
    global circle_positions
    response = jsonify(circle_positions)
    return response

@app.route('/')
def index():
    return send_from_directory('static', 'Subiaco.html')  # Subiaco.html 在当前目录


if __name__ == '__main__':
    app.run(port=5000, debug=True) 