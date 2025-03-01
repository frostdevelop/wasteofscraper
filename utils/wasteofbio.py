import requests, json, os
from wasteofdisplay import printDat

running = True
os.system('cls')
bio = input("\033[1;32m\033[1m" + "Enter new bio>" + "\033[0m")
while running:
    #name = input("\033[1;32m\033[1m" + "Enter wasteof name>" + "\033[0m")
    token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
    print("\033[0;34m\033[1m" + "Sending session request..." + "\033[0m")
    try:
        sresp = requests.get("https://api.wasteof.money/session",headers={"Authorization":token})
    except Exception as e:
        print("\033[0;31mERR: "+str(e)+"\033[0m")
        continue
    if sresp.status_code == 200:
        name = (sresp.json())["user"]["name"]
        result = requests.put("https://api.wasteof.money/users/" + name + "/bio", headers={"Authorization":token,"Content-Type":"application/json"},data=json.dumps({"bio":bio})) #,"Content-Type":"application/json" is malformed request?
        if result.status_code == 200:
            data = result.json()
            print("\033[1;33m"+"Success"+"\033[0m")
            printDat("New bio",data["bio"])
            printDat("Status",data["ok"])
        else:
            print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")    
    else:
        print("\033[0;31m"+"Session Request Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False