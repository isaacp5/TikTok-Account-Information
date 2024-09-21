import datetime

def signup_date(uid : int):
 comp = "0" + bin((uid & 0xFFFFFFFFFFFFFFFF))[2:]
 return datetime.datetime.fromtimestamp((int(comp[:32], 2)))

print("[*] Enter user_id:")
try:
 uid = int(input())
 if len(str(uid)) != 19: raise KeyboardInterrupt
except:
 print("[-] Bad user_id!"); exit()
print("[+] Sign-up date:", signup_date(uid))
