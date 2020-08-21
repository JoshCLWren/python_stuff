# Beautiful soup
# allows us to extact data from html
# does not download html we need the requests module for that
# parsing and navigating html
# htm comes back as giant string
# BeautifulSoup(html_string, "html.parser") - parses HTML
# once parsed we have ways to navigate:
# by tag name
# using find = returns one matching tag
# using find_all - returns a list of matching tags
# or css selectros

from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup) # looks like a string
print(type(soup)) #actually is an instance of a class in beautifulsoup
# the class has methods we can use
# methods:
print(soup.body) #body
print(soup.body.div) #div in a body only shows the first div
print(soup.find("div")) #still doesn't return a string, it's a element tag insntace object
print(soup.find_all("div")) #returns a list of all divs
#selecting using attributes like id or class
print(soup.find(id="first"))
print(soup.find_all(class_="special")) #class is reserved so you need the underscore returns a list of all special class
print(soup.find_all(attrs={"data-example": "yes"})) #selects bas off of attributes. You pass it a key value pair
#css selectors
# by id is by octothorp #
# by class is .
# children: div > p
# descendents: div p
print(soup.select("#first")[0]) # prints a list with the id
print(soup.select(".special")) # returns a list of classes
print(soup.selecT("[data-example=]")) #reteruns a list based of attributes

