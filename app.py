import requests
import re

keywords = ['app', 'my', 'extrac', 'bank', 'alert']
banks = ['extraco', 'navyfed', 'penfed', 'wellsfargo', 'chase']
toplevels = ['online']
alphanum = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
previous = ['castsaos.net', 'http://app-myextracalert-7f.online', 'http://appmyextracalert-5f.online']
found = []

def request_site(site):
    print(site)
    try:
        resp = requests.get(site)
        if resp.status_code == 200:
            print("x", end="")
            found.append(site)
    except requests.exceptions.ConnectionError:
        print(".", end="")
    else:
        raise RuntimeError


def find_site(sites):
    for site in sites:
        print('\n' + site)
        for x_item in alphanum:
            for y_item in alphanum:
                subx = re.sub("#X", x_item, site)
                subxy = re.sub("#Y", y_item, subx)
                request_site(subxy)

if "__main__" in __name__:
    sites = [
        'http://app-myextracalert-#X#Y.online', 
        'http://appmyextracalert-#X#Y.online',
        ]
    find_site(sites)
    if found:
        print("Found:\n------")
        for item in found:
            print('>>  ' + item)
    print("\nEnd\n")