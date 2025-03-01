import requests, json, os

def printDat(key,data):
    print("\033[1;33m\033[1m" + key + ": \033[0m\033[0;36m" + data + "\033[0m")

running = True
os.system('cls')
mode = -1
while(mode != 0 and mode != 1):
    try:
        mode = int(input("\033[1;32m\033[1m" + "Enter type (0:Love post, 1:Check if loved)>" + "\033[0m"))
    except Exception as e:
        print("Error! " + str(e))

postID = input("\033[1;32m\033[1m" + "Enter post ID>" + "\033[0m")
while running:
    token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
    match(mode):
        case 0:
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.post("https://api.wasteof.money/posts/" + postID + "/loves", headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printDat("Status",data["ok"])
                printDat("IsLoving",str(data["new"]["isLoving"]))
                printDat("LoveCount",str(data["new"]["loves"]))
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 1:
            #name = input("\033[1;32m\033[1m" + "Enter wasteof name>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            sresp = requests.get("https://api.wasteof.money/session",headers={"Authorization":token})
            if sresp.status_code == 200:
                name = (sresp.json())["user"]["name"]
                result = requests.get("https://api.wasteof.money/posts/" + postID + "/loves/" + name, headers={"Authorization":token})
                #print("https://api.wasteof.money/posts/" + postID + "/loves/" + name)
                if result.status_code == 200:
                    #data = result.json()
                    print("\033[1;33m"+"Success"+"\033[0m")
                    printDat("Loving?",result.text)
                else:
                    print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            else:
                print("\033[0;31m"+"Session Request Status: "+str(result.status_code)+"\033[0m")
    
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False