import requests, json, os
from datetime import datetime
from wasteofdisplay import printDat,printComm,promptEnum

running = True
page = 1
retries = 3
os.system('clear')
os.system('cls')
while running:
    mode = promptEnum("Category\n0:Post Comments\n1:Comment info\n2:Comment replies\n3:Report comment\n>",3)
    match(mode):
        case 0:
            postId = input("\033[1;32m\033[1m" + "Enter postID>" + "\033[0m")
            while True:
                print("\033[0;34m\033[1m" + "Sending page#" + str(page) + " request..." + "\033[0m")
                
                try:
                    result = requests.get("https://api.wasteof.money/posts/"+postId+"/comments?page="+str(page))
                except Exception as e:
                    print("\033[0;31mERR: "+str(e)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        print("\033[1;33m"+"Max retries exceeded!"+"\033[0m")
                        break
                    retries -= 1;
                    continue
                
                if result.status_code == 200:
                    data = result.json()
                    print("\033[1;33m"+"Success"+"\033[0m")
                    commlen = len(data["comments"])
                    print("\033[1;33m"+"Posts: "+"\033[0m")
                    for i in range(commlen):
                        printComm(data["comments"][i])
                        print("------")
                    
                    if(commlen == 0 or data["last"]):
                        print("\033[1;33m"+"Done!"+"\033[0m")
                        break
                    page += 1
                    retries = 3
                else:
                    print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        print("\033[1;33m"+"Max retries exceeded!"+"\033[0m")
                        break
                    retries -= 1;
        case 1:
            comID = input("\033[1;32m\033[1m" + "Enter comment ID>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/comments/" + comID)
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                printComm(data)
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 2:
            comID = input("\033[1;32m\033[1m" + "Enter comment ID>" + "\033[0m")
            while True:
                print("\033[0;34m\033[1m" + "Sending page#" + str(page) + " request..." + "\033[0m")
                
                try:
                    result = requests.get("https://api.wasteof.money/comments/"+comID+"/replies?page="+str(page))
                except Exception as e:
                    print("\033[0;31mERR: "+str(e)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        print("\033[1;33m"+"Max retries exceeded!"+"\033[0m")
                        break
                    retries -= 1;
                    continue
                
                if result.status_code == 200:
                    data = result.json()
                    print("\033[1;33m"+"Success"+"\033[0m")
                    commlen = len(data["comments"])
                    print("\033[1;33m"+"Replies: "+"\033[0m")
                    for i in range(commlen):
                        printComm(data["comments"][i])
                        print("------")
                    
                    if(commlen == 0 or data["last"]):
                        print("\033[1;33m"+"Done!"+"\033[0m")
                        break
                    page += 1
                    retries = 3
                else:
                    print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
                    print("\033[0;34m\033[1mRetry #\033[0m" + str(retries))
                    if(retries == 0):
                        print("\033[1;33m"+"Max retries exceeded!"+"\033[0m")
                        break
                    retries -= 1;
        case 3:
            commID = input("\033[1;32m\033[1m" + "Enter comment ID>" + "\033[0m")
            token = input("\033[1;32m\033[1m" + "Enter token>" + "\033[0m")
            reason = input("\033[1;32m\033[1m" + "Enter reason>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.post("https://api.wasteof.money/comments/"+commID+"/report", data=json.dumps({"type":"none","reason":reason}), headers={"Authorization":token,"Content-Type":"application/json"})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
    cont = input("\033[1;32m\033[1m" + "Next (y/n)>" + "\033[0m")
    if(cont == "n"):
        running = False