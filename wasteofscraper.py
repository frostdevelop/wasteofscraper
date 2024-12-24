import requests, json, os
from datetime import datetime

def printDat(key,data):
    print("\033[1;33m\033[1m" + key + ": \033[0m\033[0;36m" + data + "\033[0m")

running = True

while running:
    os.system('cls')
    name = input("\033[1;32m\033[1m" + "Enter wasteof username>" + "\033[0m")
    print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
    result = requests.get("https://api.wasteof.money/users/" + name)
    data = result.json()
    printDat("Name",data["name"])
    printDat("ID",data["id"])
    printDat("Bio",data["bio"])
    printDat("Verified",str(data["verified"]))
    printDat("HasAdmin",str(data["permissions"]["admin"]))
    printDat("Banned",str(data["permissions"]["banned"]))
    printDat("HasBeta",str(data["beta"]))
    printDat("Color",data["color"])
    printDat("Join Date",str(datetime.fromtimestamp(data["history"]["joined"]/1000)))
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False