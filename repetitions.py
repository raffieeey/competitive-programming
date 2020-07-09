input_string = input("")
s = list(input_string)
c = s[0]
k = 0
m = 1
for i,v in enumerate(s):
    if s[i] == c:
        k+=1
    else:
        m = max(m,k)
        k = 1
        c = s[i]

print(max(m,k))