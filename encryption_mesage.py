import random
alpha = [chr(i) for i in range(97, 123)]

a=input("Enter message u want to encrypt:")
l1 = a.split()
l2 = []

# encryption block
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

print("The encrypted message is:"," ".join(l2))

# decryption block
d=input("Enter message u want to decrypt:")
l3 = d.split()
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
        
print("The decrypted message is:"," ".join(l4))