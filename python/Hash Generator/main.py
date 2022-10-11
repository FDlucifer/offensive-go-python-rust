import hashlib

text = input("enter the text to convert into hash: ")
options = int(input('''## hash generator by lUc1f3r11
                        choose one option:
                        1) md5
                        2) sha1
                        3) sha256
                        4) sha512
                    '''))

if (options == 1):
    result = hashlib.md5(text.encode('utf-8'))
    print("the generated hash is: ", result.hexdigest())
if (options == 2):
    result = hashlib.sha1(text.encode('utf-8'))
    print("the generated hash is: ", result.hexdigest())
if (options == 3):
    result = hashlib.sha256(text.encode('utf-8'))
    print("the generated hash is: ", result.hexdigest())
if (options == 4):
    result = hashlib.sha512(text.encode('utf-8'))
    print("the generated hash is: ", result.hexdigest())
else:
    print("something went wrong")


