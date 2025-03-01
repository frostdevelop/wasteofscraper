import requests, json, os

def printDat(key,data):
    print("\033[1;33m\033[1m" + key + ": \033[0m\033[0;36m" + data + "\033[0m")

running = True
os.system('cls')
while running:
    #name = input("\033[1;32m\033[1m" + "Enter wasteof user>" + "\033[0m")
    token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
    print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
    sresp = requests.get("https://api.wasteof.money/session",headers={"Authorization":token})
    if sresp.status_code == 200:
        name = (sresp.json())["user"]["name"]
        result = requests.post("https://api.wasteof.money/users/" + name + "/surprise", headers={"Authorization":token})
        data = result.json()
        if result.status_code == 200:
            print("\033[1;33m"+"Success"+"\033[0m")
            printDat("Color",data["color"])
            printDat("Status",data["ok"])
        else:
            print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
    else:
        print("\033[0;31m"+"Session Request Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False