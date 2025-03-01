import requests, json, os
from datetime import datetime
from wasteofdisplay import printUser, printDat, promptEnum, printPost

running = True
os.system('cls')

catgs = ["users","posts"]
sorts = ["relevance"]

while running:
    query = input("\033[1;32m\033[1m" + "Query>" + "\033[0m")
    catg = promptEnum("Category 0:Users 1:Posts>",1)
    #sort = promptEnum("Sorting 0:Relevance",0)
    page = 1
    retries = 3
    while True:
        print("\033[0;34m\033[1m" + "Sending page#" + str(page) + " request..." + "\033[0m")
        try:
            result = requests.get("https://api.wasteof.money/search/" + catgs[catg] + "?q=" + query + "&sort=" + sorts[0] + "&page=" + str(page))
        except Exception as e:
            print("\033[0;31mERR: "+str(e)+"\033[0m")
            print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
            if(retries == 0):
                break
            retries -= 1;
            continue
        
        if result.status_code == 200:
            data = result.json()
            print("\033[1;33m"+"Success"+"\033[0m")
            reslen = len(data["results"])
            match(catg):
                case 0:
                    for i in range(reslen):
                        printUser(data["results"][i])
                case 1:
                    for i in range(reslen):
                        printPost(data["results"][i],False)
            
            if(reslen == 0 or data["last"]):
                break
            page += 1
            retries = 3
        else:
            print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
            if(retries == 0):
                print("\033[0;31m\033[1mMax retries exceeded\033[0m")
                break
            retries -= 1;
        
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False