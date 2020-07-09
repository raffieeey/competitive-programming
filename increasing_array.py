init=input("")
n=input("")
n=[int(i) for i in n.split()]
c=n[0]
m=0
for i,v in enumerate(n):
    if n[i] < c:
        m+=c-n[i]
    else:
        c=n[i]
print(m)