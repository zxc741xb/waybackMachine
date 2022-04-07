import webbrowser
import requests

print("Find a old website!")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Find this copy: ",old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Can't find ", site)



