a=input("Enter the value:").split()
b=[]
for i in a:
    if a.count(i)%2!=0 and i not in b:
        b.append(i)
print(b)
