# navigating with Beautiful soup
# via tags
# parent /parents
# contents
# siblings an dparents
# via searching as well

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
data = soup.body.contents #returns a list of all the elements contained therein new line \n is at the end of each part
data = soup.body.contents[1] #can't start at 0 since that would be /n
data = soup.body.contents[1].next_sibling.next_sibling #returns the next item that isn't empty
data = soup.find(class_="special").parent
data = soup.find(id="first").find_next_sibling() #reterns the next instance of an element can be chained together
data = soup.select("[data-example]")[1].find_previous_sibling(class_="special") # can pass params to searhc
data = soup.find("h3").find_parent() #all these search methods can have optional items passed to them instead of just skipping around
print(data)