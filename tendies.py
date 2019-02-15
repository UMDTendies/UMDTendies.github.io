from lxml import html
import requests

page = requests.get('http://dining.umd.edu/#specials')
tree = html.fromstring(page.content)
print("\nChecking Specials...\n")
specials = tree.xpath('//*[@id="specials"]/div[1]/div[1]/div[3]/text()')
i = 2
done = False
day = ""
while not done: 
    oldSize = len(specials)
    specials += tree.xpath('//*[@id="specials"]/div[' + str(i) + ']/div[2]/div[3]/text()') 
    if "Chicken Tenders" in specials[len(specials)-1]:
       d = tree.xpath('//*[@id="specials"]/div[' + str(i) + ']/div[2]/div[2]/span/text()') 
       day = d[0]
    if len(specials) == oldSize:
        done = True
    i += 1

day = day[:day.find('-')-1]

if day != "":
    print("Tendie day is " + day + "\n")
else:
    print("No tendies this week :(")
