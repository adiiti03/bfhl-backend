from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend communication

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        if "data" not in data:
            return jsonify({"is_success": False, "message": "Invalid Input"}), 400

        input_data = data["data"]
        numbers = [x for x in input_data if x.isdigit()]
        alphabets = [x for x in input_data if x.isalpha()]
        highest_alphabet = max(alphabets, key=str.lower) if alphabets else []

        response = {
            "is_success": True,
            "user_id": "your_name_ddmmyyyy",
            "email": "your_email@xyz.com",
            "roll_number": "YOUR_ROLL_NUMBER",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
 
