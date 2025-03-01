import requests, json, os

def printDat(key,data):
    print("\033[1;33m\033[1m" + key + ": \033[0m\033[0;36m" + data + "\033[0m")

running = True
os.system('cls')
msg = input("\033[1;32m\033[1m" + "Enter wall message>" + "\033[0m")
while running:
    name = input("\033[1;32m\033[1m" + "Enter wasteof wall user>" + "\033[0m")
    token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
    print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
    result = requests.post("https://api.wasteof.money/users/" + name + "/wall", headers={"Authorization":token,"Content-Type":"application/json"},data=json.dumps({"content":msg,"parent":None}))
    if result.status_code == 200:
        data = result.json()
        print("\033[1;33m"+"Success"+"\033[0m")
        printDat("Status",data["ok"])
        printDat("ID",data["id"])
    else:
        print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        data = result.json()
        print(data)
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False 