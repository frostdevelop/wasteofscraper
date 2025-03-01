import requests, json, os
from datetime import datetime
from wasteofdisplay import printDat,printUser,promptEnum,printPost

running = True
timeenum = ["day","week","month","all"]
os.system('cls')

while running:
    mode = promptEnum("Category 0:Trending posts 1:Top users>",1)
    match(mode):
        case 0:
            tframe = promptEnum("Timeframe 0:Day 1:Week 2:Month 3:All>",3)
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/explore/posts/trending?timeframe=" + timeenum[tframe])
            
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Timeframe",data["since"])
                for i in range(len(data["posts"])):
                    printPost(data["posts"][i],False)
                    print("------")
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 1:
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/explore/users/top");
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                for i in range(len(data)):
                    printUser(data[i])
                    print("------")
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            
        
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False