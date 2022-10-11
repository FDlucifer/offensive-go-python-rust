import whois

def is_registered(domain_name):
    try:
        d = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(d.domain_name)

if __name__ == '__main__':
    domain_name = input("enter the domain name: ")

if is_registered(domain_name):
    whois_info = whois.whois(domain_name)
    print("domain register: ", whois_info.registrar)
    print("domain server: ", whois_info.whois_server)
    print("creation date: ", whois_info.creation_date)
    print("expiration date: ", whois_info.expiration_date)
    print(whois_info)