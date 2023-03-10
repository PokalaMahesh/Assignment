from collections import Counter
top_left,first_list,second_list=[],[],[]
width,height=0,0
a=[[0 for i in range(0,4)] for j in range(0,4)]
for i in range(0,4):
    for j in range(0,4):
        a[i][j]=int(input("enter %d column and %d row"%(i,j)))
for i in range(0,4):
    for j in range(0,4):
       if a[i][j]==1:
        first_list.append(i)
        second_list.append(j)
top_left=[first_list[0],second_list[0]]
width=len(Counter(second_list).keys())
height=len(Counter(first_list).keys())
print(width)
print(height)
print(top_left)