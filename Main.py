import urllib.request
import json
import time
def getuserid(username):
    url = f"https://www.tiktok.com/api/user/detail/?uniqueId={username}"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        if "userInfo" in data:
            userid = data["userInfo"]["user"]["id"]
            return userid
        else:
            return None
    except Exception:
        return None
def main():
    username = input("[*] Enter username:")

    while True:
        user_id = get_user_id(username)
        if user_id:
            print("[+] User ID:", user_id)
            break
        else:
            print("[-] Account ID not found. Retrying in 5 seconds...")
            time.sleep(5)
if __name == "__main":
    main()
