import requests
import sys

sub_list = open("subdomains.txt").read()
subs = sub_list.splitlines()

for sub in subs:
    url_ = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(url_)

    except requests.ConnectionError:
        pass
    
    else:
        print("Valid domain: ", url_)
