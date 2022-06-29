import requests
from lxml import html

conference = "CVPR2022"

# Get the HTML text and find the classes of type 'ptitle'
response = requests.get("http://openaccess.thecvf.com/"+conference+"?day=all")
tree = html.fromstring(response.text)
print(response)
papers = tree.find_class('ptitle')

# Get all titles in a list
all_titles = []
for paper in papers:
    title = paper.xpath('a/text()')
    all_titles.append(title[0])

# Print to file
f = open(conference + '.txt', 'w')
for title in all_titles:
    f.write(title+'\n')
f.close()