from socket import *
import optparse
import threading

def portscan(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((host, int(port)))
        print(host, " tcp/" + str(port) + " open")
    except:
        print(host, " tcp/" + str(port) + " closed")

def main():
    parser = optparse.OptionParser("usage%prog " + "-H <specify target host> -p <specify target port>")
    parser.add_option("-H", "--host", dest="targethost", type="string", help="specify target host")
    parser.add_option("-p", "--ports", dest="targetport", type="string", help="specify target port")

    option, args = parser.parse_args()

    thost = option.targethost
    tports = str(option.targetports).split(",")

    if thost == None or tports[0] == None:
        print(parser.usage)
        exit(0)

    setdefaulttimeout(1)
    host_ip = gethostbyname(thost)

    for port in tports:
        t = threading.Thread(target=portscan, args=(thost, port))
        t.start()
        # portscan(host_ip, port)

main()