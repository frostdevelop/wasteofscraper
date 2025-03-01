import requests, json, os
from datetime import datetime
from wasteofdisplay import printDat

running = True
os.system('cls')
token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
while running:
    user = input("\033[1;32m\033[1m" + "Enter user>" + "\033[0m")
    print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
    try:
        result = requests.post("https://api.wasteof.money/users/"+user+"/ban", headers={"Authorization":token})
    except Exception as e:
        print("\033[0;31mERR: "+str(e)+"\033[0m")
        continue
    if result.status_code == 200:
        data = result.json()
        print("\033[1;33m"+"Success"+"\033[0m")
        print(data)
        if("error" in data.keys()):
            printDat("Error",data["error"])
        else:
            printDat("Action",data["ok"])
    else:
        print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False