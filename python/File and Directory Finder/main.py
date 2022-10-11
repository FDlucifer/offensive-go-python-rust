from colorama import init, Fore
import requests

init()
class color:
    red = Fore.RED
    bule = Fore.BLUE
    green = Fore.GREEN
    yellow = Fore.YELLOW
    cyan = Fore.CYAN
    error = Fore.RED + "[" + Fore.RESET + "-" + Fore.RED + "]" + Fore.RESET + " "
    adv = Fore.YELLOW + "[" + Fore.RESET + "-" + Fore.YELLOW + "]" + Fore.RESET + " "
    ble = Fore.BLUE + "[" + Fore.RESET + "-" + Fore.BLUE + "]" + Fore.RESET + " "
    reset = Fore.RESET

header = {'User-Agent': 'Mozilla/5.0'}
wordlist = input("enter the wordlist directory: ")
target = input("enter the url like (http://example.com): ")
found = []

def urlfuzz(url, mylist):
    words = []
    with open(mylist, 'r', encoding="latin1") as wl:
        for line in wl:
            words.append(line.rstrip('\n'))
        for word in words:
            if word == "":
                pass
            else:
                targetweb = url + word
                response = requests.get(targetweb, headers=header)
                status = response.status_code
                if status in range(200, 299):
                    print(targetweb + color.green + " ---> found " + color.reset)
                    found.append(targetweb)
                else:
                    print(targetweb + color.red + " ---> not found " + color.reset)

if __name__ == "__main__":
    urlfuzz(target, wordlist)
    print("\n[* discovered info *]")
    for inf in found:
        print(inf + color.green + " ---> found " + color.reset)
