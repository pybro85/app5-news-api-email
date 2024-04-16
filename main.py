import requests 

api_key="88970df1b20840ef82308e861c561b0e"
url = "https://newsapi.org/v2/everything?q=apple&from=2024-04-15&to=2024-04-15&sortBy=popularity&apiKey=88970df1b20840ef82308e861c561b0e"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
print(content)


# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])


