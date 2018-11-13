import urllib.request
import bs4 as bs
import json 
url = urllib.request.urlopen('https://edraft.com/nfl/stats/leaders/').read() #so this link searches for all content on this url. 
soup = bs.BeautifulSoup(url,'lxml')
stats = [] #storing data here. 
#rows =  soup.find("t", { "class" : "mod-content" }).find('tr'),

for data in soup.select(".Container"):
    a = str(data.text)
    stat = data.find("td", attrs={"class": "TextLeft Name"})
    stat1 = data.find_all("TextLeft Name")
    myList = []
    count = 0
    for link in data.find_all("td", attrs={"class": "TextLeft Name"}):
        player = "player"
        player = '{}{}'.format(player, count)
        count += 1
        playerData = player +": " + link.text +" Count: " + link.next_sibling.get_text()
        myList.append(playerData)
    #print(myList)
    #stats.append(a) 
    record = {
        "title": data.td.get_text(),
        "top_player": stat.get_text() +' ' + stat.next_sibling.get_text(),
        "all_stats ": myList
    }
    stats.append(record)
#print(*stats, sep='\n')
print(json.dumps({"nfldata": stats}, indent=3))



#making the file so you can read it in your script. 
with open("nflstats.json", "w") as writeJSON:
    json.dump(json.dumps({"nfldata": stats}, indent=3), writeJSON, ensure_ascii=False)

