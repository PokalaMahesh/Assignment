# For the given array   WAP to divide each number of the array by the next number. Divide the last number by first number of array. 
# Provide proper exceptional handling for 0.
a=[9,33,0,7,2,82,77]
b=[]
for i in range(0,len(a)):
    if i==len(a)-1:
        if a[0]==0:
            result='infinity'
            b.append(result)
            continue
        result=a[len(a)-1]/a[0]
        print(result)
    if i!=len(a)-1:
        if a[i+1]==0:
            result='infinity'
            b.append(result)
            continue
        else:
            result=a[i]/a[i+1]
            print(result) 
    b.append(result)
print(b)