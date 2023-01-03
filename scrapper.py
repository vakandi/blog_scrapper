import requests
from bs4 import BeautifulSoup

# URL of the blog website you want to scrape
url = "http://www.example.com/blog"

# Send a GET request to the website and retrieve the HTML
response = requests.get(url)
html = response.text

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all the main articles on the page
main_articles = soup.find_all('article', class_='main-article')

# Create an empty list to store the articles
articles = []

# Iterate through the main articles and extract the title and content
for article in main_articles:
  title = article.h2.text
  content = article.p.text

  # Store the title and content in a dictionary
  articles.append({'title': title, 'content': content})

# Create the HTML for the website
html = """
<html>
<head>
  <title>Scraped Articles</title>
</head>
<body>
  <h1>Scraped Articles</h1>
"""

# Add the articles to the website
for article in articles:
  html += """
  <article>
    <h2>{}</h2>
    <p>{}</p>
  </article>
  """.format(article['title'], article['content'])

html += """
</body>
</html>
"""

# Save the HTML to a file
with open('articles.html', 'w') as file:
  file.write(html)

