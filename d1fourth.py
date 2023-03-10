b=int(input("enter the number of persons"))
a = [0] * b
for i in range(b):
    a[i] = i + 1
pos = 0
while (len(a) > 1):
    pos += 1
    print("pos number",pos)
    print("length of the a",len(a))
    pos %= len(a) 
    print("delete element",a[pos])
    del a[pos]
print(a[0])