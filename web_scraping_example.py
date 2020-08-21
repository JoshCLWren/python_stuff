# requests + beautiful soup example
# goal: grab all links from rithm school blog
#  data collect dates and articale titles into csv

import requests
from csv import writer
from bs4 import BeautifulSoup

response = requests.get("https://www.rithmschool.com/blog")
soup = BeautifulSoup(response.text, "html.parser")
# select all artical tags
articles = soup.find_all("article")

with open("blog_data.csv", "w") as csv_file:
  csv_writer = writer(csv_file)
  csv_writer.writerow(["title","link","data"])
  for article in articles:
    # loop over the articles and grab the first anchor tag which will have the title
    a_tag = article.find("a")
    title = a_tag.get_text()
    url = a_tag['href']
    date = article.find("time")["datetime"]
    csv_writer.writerow([title, url, date])


