import getpass
import base64

u=input("enter your username:")
p=getpass.getpass(prompt="Enter your password:")
creds=u+'.'+p
def encryptcrediential(pwd):
    value=base64.b64encode(pwd.encode())
    return value
def decryptcredientials(pwd):
    value=base64.b64decode(pwd.decode())
    return value
x=encryptcrediential(p)
print("simple creds: "+p)
print("encrypted credientials: ", x)
print("decrypted credientials: ", decryptcredientials(x))
