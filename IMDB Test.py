import requests

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"salman khan"}

headers = {
	"X-RapidAPI-Key": "c0ceeccd85mshf1786a5dfc95c66p1c85dejsn4d2040ffbbbe",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"

headers = {
	"X-RapidAPI-Key": "c0ceeccd85mshf1786a5dfc95c66p1c85dejsn4d2040ffbbbe",
	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())