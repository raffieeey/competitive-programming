n=int(input(""))
print(int(n))
while n>1:
    if n%2 == 0:
        n/=2
    else:
        n=n*3+1
    print(int(n))
    