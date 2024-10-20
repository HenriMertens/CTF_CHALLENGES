from string import printable

#extracted from java
encryptedurl =[
            42, 6, 68, 64, 7, 120, 93, 31, 83, 17,
            48, 23, 81, 92, 90, 46, 11, 68, 68, 27,
            44, 30, 81, 82, 7, 108, 29, 66, 87, 91,
            33, 23, 66, 85, 21, 46, 1, 31, 86, 6,
            45, 29, 68, 82, 6, 45, 29, 68, 30, 30,
            50, 23, 87]

#we know url has this prefix
url = "https://"

#ascii value of url
url_bytes = [104, 116, 116, 112, 115, 58, 47, 47]


passw = ""

#xoring the bytes
for i in range(len(url)):
    for c in printable:
        if(encryptedurl[i] ^ ord(c) == url_bytes[i]):
            passw += c
            break

#making sure it happend correct, we should see "https" being printed"
testpass = ""
def test(passw, j):
    return chr(ord(passw) ^ encryptedurl[j])

for i in range(len(passw)):
    testpass += test(passw[i], i)



print(passw)
print(testpass)
#print the length
print(len(encryptedurl))
