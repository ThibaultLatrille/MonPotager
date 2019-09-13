import requests
from lxml import html
import re

home_url = "https://sage-pdb.herokuapp.com"
page_url = home_url + "?page={0}"
search_url = home_url + "/search/{0}"
export_url = home_url + "/export_plant_data/"
session = requests.Session()
text = session.get(page_url).text
match = "Page 1 of "
nbr_pages = int(text[text.find(match) + len(match):].split("\n")[0])
print("{0} pages to fetch.".format(nbr_pages))

names = set()
for page_nbr in range(1, nbr_pages + 1):
    page_get = session.get(page_url.format(page_nbr))
    tree = html.fromstring(page_get.content)
    xpath = tree.xpath('//div[@class="row plantname"]/div/text()')
    for index in range(len(xpath) // 2):
        name = re.sub('[^0-9a-zA-Z]+', ' ', re.sub(r'\([^)]*\)', '', xpath[index * 2][:-1])).split(" ")[0].lower()
        if len(name) > 2:
            names.add(name)
    print("Page {0} visited.".format(page_nbr))

print("{0} names to export.".format(len(names)))
headers = set()
lines = set()

for i, name in enumerate(names):
    print("{0:.2f}% exported.".format(100 * (i + 1) / len(names)))
    search_get = session.get(search_url.format(name))
    export_text = session.get(export_url).text
    if "!DOCTYPE html" not in export_text:
        export_lines = export_text.split("\n")
        headers.add(export_lines[0])
        lines.update([i.capitalize() for i in export_lines[1:]])

csv_file = open("sage.csv", "w")
csv_file.writelines(headers)
csv_file.writelines(sorted(lines))
csv_file.close()


assert(len(lines) > 0)
assert(len(headers) == 1)
