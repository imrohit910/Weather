import requests
def	weather(query):

	url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

	querystring = {"city": "Seattle"}

	headers = {
		"X-RapidAPI-Key": "################",
		"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=query)
	return response.json()



