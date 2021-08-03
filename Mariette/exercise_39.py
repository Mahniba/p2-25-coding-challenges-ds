def generate_key(n):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for c in chars:
        key[c]=chars[(cnt + n )% len(chars)]
        cnt+=1
    return key


def encrypt(key,message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher
def get_decrypt_key(key):
    dkey = {}
    for k in key:
        dkey[key[k]] = k
        return dkey

key = generate_key(4)
dkey = generate_key(22)
cipher = encrypt (key, "YOU CAN DO IT")
print(cipher)
message = encrypt(dkey,cipher)
print(message)
dkey = get_decrypt_key(key)
print(encrypt(dkey,cipher))