import requests, json, os

def printDat(key,data):
    print("\033[1;33m\033[1m" + key + ": \033[0m\033[0;36m" + data + "\033[0m")

running = True
os.system('cls')
user = input("\033[1;32m\033[1m" + "Enter wasteof username>" + "\033[0m")
while running:
    while True:
        print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
        result = requests.get("https://api.wasteof.money/users/"+user+"/posts", data={"page":i})
        if result.status_code == 200:
            data = result.json()
            print("\033[1;33m"+"Success"+"\033[0m")
            printDat("Id",str(data["id"]))
            printDat("Action",str(data["ok"]))
        else:
            print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False