import googlemaps
import urllib.request

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
api_key = 'AIzaSyArYxO5XWE9L8N_W77G8B8-qXiDuTqlVWI'
gmaps = googlemaps.Client(key=api_key)

def download_street_view_image(location, timestamp, heading=0, pitch=0, fov=90, size=(600, 400), output_file='street_view_image.jpg'):
    """
    Download a historical Street View image of a specific location.

    :param location: (dict) Dictionary containing 'lat' and 'lng' keys representing the location.
    :param timestamp: (int) The timestamp representing the desired date for the historical image.
    :param heading: (float) The compass heading (in degrees) of the camera. Default is 0.
    :param pitch: (float) The up or down angle of the camera. Default is 0.
    :param fov: (float) The field of view of the camera. Default is 90.
    :param size: (tuple) Tuple containing the width and height of the image. Default is (600, 400).
    :param output_file: (str) Name of the output file. Default is 'street_view_image.jpg'.
    """
    street_view_url = f"https://maps.googleapis.com/maps/api/streetview?location={location['lat']},{location['lng']}&size={size[0]}x{size[1]}&fov={fov}&heading={heading}&pitch={pitch}&key={api_key}&timestamp={timestamp}"
    urllib.request.urlretrieve(street_view_url, output_file)
    print(f"Historical Street View image downloaded and saved as {output_file}")

def main():
    # Replace '1600 Amphitheatre Parkway, Mountain View, CA' with your desired address
    address = '55 Ashford Street, Alston, MA'

    # Get geolocation data for the address
    geocode_result = gmaps.geocode(address)

    if not geocode_result:
        print("Geolocation not found for the given address.")
        return

    # Extract latitude and longitude from geolocation data
    location = geocode_result[0]['geometry']['location']

    # Replace 'desired_timestamp' with the timestamp of the desired date (in seconds since the epoch)
    desired_timestamp = 1420070400  # Example: January 1, 2015.
    # It may still get the same image as not everywhere has a historical image

    # Download historical Street View image
    download_street_view_image(location, timestamp=desired_timestamp)

if __name__ == "__main__":
    main()