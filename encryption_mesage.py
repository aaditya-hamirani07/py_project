import random
alpha = [chr(i) for i in range(97, 123)]

# Function for encrypting messages
def encryption_block(x):
    l1 = x.split()
    l2 = []

    for i in l1:
        b = ""
        c = ""
        if(len(i)>=3):
            pre = ""
            post = ""

            b = i[1::] + i[0]
            
            for j in range(3):
                pre += random.choice(alpha)

            for j in range(3):
                post += random.choice(alpha)

            c = pre + b + post
            l2.append(c)
        else:
            l2.append(i[::-1])
    
    return l2

# Function for decrypting message
def decryption_block(y):
    l3 = y.split()
    l4 = []

    for p in l3:
        m=""
        n=""
        if(len(p)<3):
            l4.append(p[::-1])
        else:
            m = p[3:-3]
            n = m[-1] + m[0:-1]
            l4.append(n)
    
    return l4

while True:
    print("Enter 1 to encrypt,2 to decrypt,0 to exit: ",end="")
    num = int(input())
    if(num==1):
        a=input("Enter message u want to encrypt:")
        encrypted_list = encryption_block(a)
        print("The encrypted message is:"," ".join(encrypted_list))
    elif(num==2):
        d=input("Enter message u want to decrypt:")
        decrypted_list = decryption_block(d)
        print("The decrypted message is:"," ".join(decrypted_list))
    elif(num==0):
        print("Program exit...")
        break
    else:
        print("Invalid ,please enter 1,2 or 0")
