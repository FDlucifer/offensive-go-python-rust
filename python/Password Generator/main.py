import random

print("password generator")

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=?\/<>,."

pnum = int(input("how many password you want to generate: "))
plen = int(input("what is the passwords size: "))

print("generated passwords!!")
print()

for password in range(pnum):
    passwords = ""
    for i in range(plen):
        passwords += random.choice(alpha)
    print(passwords)

