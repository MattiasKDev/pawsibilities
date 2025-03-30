from flask import Flask, jsonify, request
from browser import run_scraper
import asyncio

# from browser import Browser  # Assuming browser.py contains a class named Browser

app = Flask(__name__)

@app.route('/data', methods=['POST'])
async def get_data():
    # Parse the JSON body from the request
    body = request.get_json()
    if not body or not all(key in body for key in ['query', 'long', 'lat']):
        return jsonify({"error": "Invalid input"}), 400

    # Extract data from the request body
    name = body['query']
    longitude = body['long']
    latitude = body['lat']

    data = await run_scraper(name, longitude, latitude)
    return jsonify(data)

    # Create an instance of the Browser class
    # browser = Browser()

    # Fetch data using a method from the Browser class (pass the extracted data if needed)
    # data = browser.get_data(name=name, longitude=longitude, latitude=latitude)  # Adjust method signature as needed
    data = ''
    # Return the data as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)