# /* There are 100 man making a circle each man is wearing a T-shit with a number 1 to 100  in series. Person with Number 1 on 
# his/her T-Shirt got a gun now 1 kill 2 and give that gun to 3 and then 3 kill 4 and give that gun to 5.. then so on 99 killed 100
#  and give that gun again to 1 WAP to find which man is left with a gun on his hand at the end ?? */
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