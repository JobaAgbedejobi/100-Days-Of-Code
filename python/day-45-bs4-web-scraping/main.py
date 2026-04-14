from bs4 import BeautifulSoup
# Sometimes you may have to use the lmxl's parser instead of html. If so import lxml and

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser') # replace html parser with lxml

# Soup is now an object that allows us to tap into various parts of "website.hmtl"
# but using python code instead. Soup treats the html like python code basically

# i.e. if you wanted the title tag from website.html:
# print(soup.title) # Prints out the title, including the elements
# print(soup.title.name) # Gives you the name of the title tag, in this case it's title
# print(soup.title.string) # Print's the actual title itself without the tags

# print(soup.prettify()) # Basically the same as print(contents)

# #print(soup.{INSERT ANY TAG}) prints out the first object with that type of tag i.e.
# print(soup.a) # prints: <a href="https://www.appbrewery.co/">The App Brewery</a>
# print(soup.li) # prints: <li>The Complete iOS App Development Bootcamp</li>

# The 'find.all' method allows for you to find all of a particular thing. We can use it
# to find all of the anchor tags e.g.
all_anchor_tags = soup.find_all(name="a")

# There is a method '.getText' that allows you to draw out string from any element
# i.e.
# for tag in all_anchor_tags:
#     print(tag.getText())

# There is a method called '.get' which allows you to get the value of an attribute
# i.e.
# for tag in all_anchor_tags:
#     print(tag.get("href"))

# You can use '.find' method to search by attribute instead of name
# i.e.
# heading = soup.find(name="h1", id="name")
# print(heading)

# However when looking for a class, you need to use the parameter 'class_' because
# you can only use 'class' when creating a class. This doesn't change the fact that
# you can use "class" for the get method as it's a string, not a parameter

# 'select_one' method returns the first matching item and 'select' will return all
# matching items in a list. 'Selector' parameter requires a string of the name of
# whatever you're looking for and its special symbol

# i.e. for element selector:
# company_url = soup.select_one(selector="p a")
# print(company_url)
# It's similar to if you were to make a css style for that particular line, how would
# you find it? You'd do p a {
# ...} because the anchor tag sits in the paragragh tag so same here

# i.e. for id selector:
# company_url = soup.select_one(selector= "#name")
# print(company_url)
# # is the special symbol for an id and name is the name of the id we're looking for

# i.e. for class elements with name "heading":
# headings = soup.select(".heading")
# print(headings)
# (no need for keyword arguments as selector is the 1st parameter)

# FIND_ALL() vs. SELECT():
# find_all() is generally slightly faster for simple searches
# select() is more powerful for complex patterns

# Start with find_all() for simple cases
# Switch to select() when you need CSS selector power
# If you know CSS well, you might prefer select() for everything
# The choice often comes down to personal preference and what feels more natural to you!