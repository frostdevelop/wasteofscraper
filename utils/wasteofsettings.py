import requests, json, os, getpass
from wasteofdisplay import printDat, promptEnum
    
running = True
os.system('cls')
"""
return (r = new FormData).append("banner", n),
t.next = 4,
fetch("".concat("https://api.wasteof.money", "/users/").concat(e.user, "/banner"), {
    method: "PUT",
    headers: {
        Authorization: e.$auth.token
    },
    body: r
}
https://api.wasteof.money/users/ko/picture
https://api.wasteof.money/users/ko/banner
fetch("".concat("https://api.wasteof.money", "/users/").concat(t.user, "/picture"), {
    method: "PUT",
    headers: {
        Authorization: t.$auth.token
    },
    body: r
}).then((function(t) {
    return t.json()
}
"""
authenum = ["google","github","password"]
while running:
    token = input("\033[1;32m\033[1m" + "Enter wasteof token>" + "\033[0m")
    mode = promptEnum("Mode\n0:Show settings\n1:Hide recovery message\n2:Delete banner\n3:Change name\n4:Change email\n5:Delete email\n6:Disable auth method\n7:Enable auth method\n8:Delete Auth Method\n9:Change passcode\n10:Suprise (Randomize User Color)\n>",10)
    match(mode):
        case 0:
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.get("https://api.wasteof.money/settings", headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                #print(data)
                printDat("Email enabled",str(data["email"]["hasEmail"]))
                if("password" in data["auth"].keys()):
                    printDat("Password Enabled",str(data["auth"]["password"]["enabled"]))
                if("google" in data["auth"].keys()):
                    printDat("Google Enabled",str(data["auth"]["google"]["enabled"]))
                    printDat("Google ID",str(data["auth"]["google"]["id"]))
                if("github" in data["auth"].keys()):
                    printDat("Github Enabled",str(data["auth"]["github"]["enabled"]))
                    printDat("Github ID",str(data["auth"]["github"]["id"]))
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 1:
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.post("https://api.wasteof.money/settings/hide-recovery-message", headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 2:
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            sresp = requests.get("https://api.wasteof.money/session",headers={"Authorization":token})
            if sresp.status_code == 200:
                name = (sresp.json())["user"]["name"]
                result = requests.delete("https://api.wasteof.money/users/"+name+"/banner", headers={"Authorization":token})
                if result.status_code == 200:
                    data = result.json()
                    print("\033[1;33m"+"Success"+"\033[0m")
                    if("error" in data.keys()):
                        printDat("Error",data["error"])
                    else:
                        printDat("Action",data["ok"])
                else:
                    print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            else:
                print("\033[0;31m"+"Session Request Status: "+str(result.status_code)+"\033[0m")
        case 3:
            neo = input("\033[1;32m\033[1m" + "Enter new name>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            sresp = requests.get("https://api.wasteof.money/session",headers={"Authorization":token})
            if sresp.status_code == 200:
                name = (sresp.json())["user"]["name"]
                result = requests.put("https://api.wasteof.money/users/"+name+"/name", data=json.dumps({"name":neo}), headers={"Authorization":token,"Content-Type":"application/json"})
                if result.status_code == 200:
                    data = result.json()
                    print("\033[1;33m"+"Success"+"\033[0m")
                    if("error" in data.keys()):
                        printDat("Error",data["error"])
                    else:
                        printDat("Action",data["ok"])
                        printDat("New name",data["name"])
                else:
                    print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
            else:
                print("\033[0;31m"+"Session Request Status: "+str(result.status_code)+"\033[0m")
        case 4:
            neo = input("\033[1;32m\033[1m" + "Enter new email>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.put("https://api.wasteof.money/settings/email", data=json.dumps({"email":neo}), headers={"Authorization":token,"Content-Type":"application/json"})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 5:
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.delete("https://api.wasteof.money/settings/email", headers={"Authorization":token})
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 6 | 7 | 8:
            authmethod = promptEnum("Method\n0:Google\n1:Github\n2:Password\n>",2)
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = (requests.delete("https://api.wasteof.money/settings/auth/"+authenum[authmethod], headers={"Authorization":token}) if(mode==8) else requests.post("https://api.wasteof.money/settings/auth/"+authenum[authmethod]+("/disable" if(mode==6) else "/enable"), headers={"Authorization":token}))
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                #print(data)
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 9:
            npass = getpass.getpass("\033[1;32m\033[1m" + "Enter new password>" + "\033[0m")
            print("\033[0;34m\033[1m" + "Sending request..." + "\033[0m")
            result = requests.put("https://api.wasteof.money/settings/auth/password", headers={"Authorization":token,"Content-Type":"application/json"}, data=json.dumps({"password":npass}))
            if result.status_code == 200:
                data = result.json()
                print("\033[1;33m"+"Success"+"\033[0m")
                #print(data)
                if("error" in data.keys()):
                    printDat("Error",data["error"])
                else:
                    printDat("Action",data["ok"])
            else:
                print("\033[0;31m"+"Status: "+str(result.status_code)+"\033[0m")
        case 10:
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