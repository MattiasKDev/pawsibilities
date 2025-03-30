import asyncio

from flask import Flask, jsonify, request
from flask_cors import CORS

from browser import run_scraper

# from browser import Browser  # Assuming browser.py contains a class named Browser

app = Flask(__name__)
CORS(app)
@app.route('/data', methods=['POST'])
async def get_data():
#     return [
#     {
#         "address": "4065 Harvester Rd, Burlington, ON L7L 5J1",
#         "hours": "10 a.m.–1 a.m. (Sun-Thu), 10 a.m.–2 a.m. (Fri-Sat)",
#         "name": "Burlington Bowl",
#         "pricing": "Not available",
#         "website": "http://www.burlingtonbowl.com/"
#     },
#     {
#         "address": "3055 Dundas St W, Mississauga, ON L5L 3R8",
#         "hours": "9 a.m.–11 p.m. (Sun-Thu), 9 a.m.–12 a.m. (Fri-Sat)",
#         "name": "Classic Bowl",
#         "pricing": "$80+ for four people to bowl one game in an hour",
#         "website": "http://www.classicbowl.com"
#     },
#     {
#         "address": "830 Laurentian Dr, Burlington, ON L7N 3V6",
#         "hours": "10 a.m.–11 p.m. (Sun-Thu), 10 a.m.–1 a.m. (Fri-Sat)",
#         "name": "Splitsville Burlington",
#         "pricing": "Not specified",
#         "website": "https://splitsville.ca/burlington-bowling/"
#     },
#     {
#         "address": "1515 Rebecca St, Oakville, ON L6L 5G8",
#         "hours": "12–6 p.m. (Sun), 12–9 p.m. (Mon-Wed, Fri), 4–9 p.m. (Thu), 10:30 a.m.–9 p.m. (Sat)",
#         "name": "Hopedale Bowl",
#         "pricing": "Unknown",
#         "website": "http://www.hopedalebowl.ca/"
#     }
# ]
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
