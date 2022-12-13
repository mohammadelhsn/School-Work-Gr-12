import requests

# Make a request to the API's server
response = requests.get('https://api.weather.com/v1/geocode/40.7128/-74.0060/observations.json')

# Check the response status code to make sure the request was successful
if response.status_code == 200:
  # Print the weather data
  print(response.json())
else:
  # Print an error message if the request failed
  print(f'Error: {response.status_code}')