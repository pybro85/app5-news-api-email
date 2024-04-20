import requests
from send_email import send_email 

topic = "Tesla"
api_key="88970df1b20840ef82308e861c561b0e"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-03-20&" \
      "sortBy=publishedAt&"\
      "apiKey=88970df1b20840ef82308e861c561b0e&" \
      "language=en"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
# print(content)
message = ""
# Access the article titles and description
for article in content["articles"][:20]:
    # message = message + f"""\
             
    # Title: {article["title"]}
    # Description: {article["description"]}    
    
    # """
    if article["title"] and article["description"] is not None:
        message = "Subject: Today's news" + "\n" + message + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

message = message.encode("utf-8")
send_email(message)
    # print(article["title"])
    # print(article["description"])


