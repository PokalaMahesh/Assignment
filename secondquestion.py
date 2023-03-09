# Find the sum of all the numbers in a string which is divisible by 3 and also find the last such number, Example 
# "The best 6 of 8 will get 9 points", sum = 12, last=9
input=input("enter the string")
a=[int(s) for s in input.split() if s.isdigit()]
sum=0
for i in range(len(a)):
    if a[i]%3==0:
        sum +=a[i]
        last_num=a[i]
print("the sum is %d and last number is %d"%(sum,last_num))
