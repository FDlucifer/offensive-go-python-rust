import requests
import re

print('[-] email finder [-]')
print('')

to_craw = []
to_craw.append(input("domain target: "))

if to_craw[0].startswith('www'):
    to_craw[0] = 'http://' + to_craw[0]

crawled = set()
emails = set()

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' 'AppleWebKit/537.36 (KHTML, like Gecko)' 'Chrome/106.0.0.0 Safari/537.36'}

for i in range(15):
    url = to_craw[0]
    try:
        req = requests.get(url, headers=header)
    except Exception as e:
        print(e)
        to_craw.remove(url)
        crawled.add(url)
        continue

    html = req.text
    links = re.findall(r'<a href="?\'?(https?:\/\/[^"\'>]*)', html)
    emails = re.findall(r'[\w\._-]+@[\w\._-]+\.[\w\._-]+\w', html)
    print("looking for ... ", url)

    to_craw.remove(url)
    crawled.add(url)

    for link in links:
        if link not in crawled and links not in to_craw:
            to_craw.append(link)

    for email in emails:
        emails_found.add(email)

print('\n[+] emails found: ')
for email in emails_found:
    print(email)
