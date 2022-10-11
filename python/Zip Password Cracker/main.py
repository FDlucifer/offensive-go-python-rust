import zipfile

obj = zipfile.ZipFile("test.zip")

f = open("password.txt", 'r')

for password in f.readlines():
    password = password.strip("\n").strip("\r")

    try:
        obj.extractall(pwd=password)
        print("password found: " + password + " <<<<<<<<<<<<<<<<<")
    except:
        print("trying......")