from operator import indexOf

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)
article_tags = soup.find_all(class_ = "titleline")
article_texts = []
article_links = []
for article in article_tags:
    article_tag = article.find(name="a")
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href") # OR article["href"] - you can access HTML
    # attributes with square brackets, similar to dictionary keys
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all
(name = "span", class_ = "score")]


# HOW TO GET THE MOST POPULAR ONE (HIGHEST UPVOTE)

#THIS WAS BEFORE I LOOKED AT THE SOLUTION - DIDN'T KNOW THERE WAS AN '.INDEX' METHOD
# mau = -1
# for vote in article_upvotes:
#     mau+=1
#     if vote == max(article_upvotes):
#         index = mau

# ---------------- OR ------------------

maximum = max(article_upvotes)
index = article_upvotes.index(maximum)

print(article_texts[index])
print(article_links[index])
print(article_upvotes[index])
