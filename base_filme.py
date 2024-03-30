import base64

txt = input("Please enter txt:")

#base16
try:
    print(base64.b16decode(txt).decode())
except:
    print('Not base16')
#base32
try:
    print(base64.b32decode(txt).decode())
except:
    print('Not base32')
#base64
try:
    print(base64.b64decode(txt).decode())
except:
    print('Not base64')
#base85
try:
    print(base64.b85decode(txt).decode())
except:
    print('Not base85')
