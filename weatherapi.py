import requests
def	weather(query):

	url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

	querystring = {"city": "Seattle"}

	headers = {
		"X-RapidAPI-Key": "16f6e00746msh9d310980b0cde54p157b7fjsn1385f9e4a29d",
		"X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=query)
	return response.json()



