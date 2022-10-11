import crypt

f = open("password.txt", "r")

for word in f.readline():
    word = word.strip("\n")
    hash = crypt.crypt(word, "$6$8HOLitkI")
    if hash == "":
        print("password found: ", word)
    else:
        print("trying...")

