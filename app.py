from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/character', methods=['POST'])
def get_character():
    try:
        data = request.get_json()
        id = str(data.get('character_id'))

        if not id:
            return jsonify({"error": "No character ID provided"}), 400

        response = requests.get("https://rickandmortyapi.com/api/character/" + id)
        
        if response.status_code == 404:
            return jsonify({"error": "Character not found"}), 404

        character_data = response.json()
  
        return jsonify({
            "name": character_data.get('name'), "status": character_data.get('status')
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
