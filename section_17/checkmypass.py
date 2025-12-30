import requests
import hashlib
from sys import argv

# Reworked to use list comprehension...
#
# def find_pw_index(pw_list, pw_hash):
#     for i, line in enumerate(pw_list):
#         if pw_hash.upper() in line.upper():
#             return i
#     return -1


def get_pw_leaked_count(pw_list, pw_hash):
    hashes = (lines.split(':') for lines in pw_list.splitlines())
    for hash, count in hashes:
        if pw_hash.upper() == hash.upper():
            return int(count)
    return 0


def get_hashes_from_api(pw_hash):
    url = "https://api.pwnedpasswords.com/range/" + pw_hash
    res = requests.get(url)
    return res.text


def check_password(password):
    encoded_pw = password.encode("UTF-8")
    hashed_pw = hashlib.sha1(encoded_pw).hexdigest()
    pw_hashes_in_db = get_hashes_from_api(hashed_pw[:5])
    return get_pw_leaked_count(pw_hashes_in_db, hashed_pw[5:])


if __name__ == "__main__":
    if len(argv) > 1:
        for password in argv[1:]:
            times_in_db = check_password(password)
            if times_in_db > 0:
                print(f"You are pwnd, password {password} found {times_in_db} times in database")
            else:
                print(f"Lucky! password {password} not pwnd (yet)")
