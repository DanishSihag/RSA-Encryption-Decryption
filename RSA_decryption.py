from ext_euc import ext_euc

def encryption(e,n,message):
    cipher= ""                                    #initiate cipher text as empty

    for c in message:                             #go through each character
        m = ord(c)                                # to get the unicode value of the character
        cipher = cipher + str(pow(m,e,n)) + " "

    return cipher


def decryption(d,n,cipher):
    message = ""                                  #initialise message as empty
    characters = cipher.split()                   #to make each character seoarated avoid confusion
    for i in characters:
        c = int(i)                                #convert the text to integer, value not actually rerquired, just for message value / print(c)
        message = message + chr(pow(c,d,n))       #convert again to string to get the message back

    return message


def generate_key(p,q,e):
    n=p*q
    phiN = (p-1)*(q-1)

    gcd,d,y=ext_euc(e,phiN)                         #getting the simplification for d.e=1mod(phi(n))
    d=d%((p-1)*(q-1))                               #from online notes, to get actual updated value of d

    message = "Danish Sihag"
    x = encryption(e,n,message)
    y = decryption(d,n,x)

    print(f"d = {d}")
    print(f"e = {e}")
    print(f"n = {n}")
    print(f"text = {message}")
    print(f"encrypted value of text = {x}")
    print(f"decrypted value of text = {y}")

generate_key(,547,47)
