import requests, os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("MAPS_API_KEY")

def get_address(lat: float, lon: float) -> str:
    """
    Get the address for the given latitude and longitude using the reverse geocoding API.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.

    Returns:
        str: A formatted string containing the house number, road, and postal code, or an error message.
    """
    api_url = f"https://geocode.maps.co/reverse?lat={lat}&lon={lon}&api_key={key}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        address = data.get("address", {})
        house_number = address.get("house_number", "")
        road = address.get("road", "")
        postcode = address.get("postcode", "")
        if house_number and road and postcode:
            return f"{house_number}, {road}, {postcode}"
        else:
            return "Address details not complete"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Example usage
# if __name__ == "__main__":
#     latitude = 43.436348
#     longitude = -79.747566
#     address = get_address(latitude, longitude)
#     print(address)  # Print only the house number, road, and postal code
