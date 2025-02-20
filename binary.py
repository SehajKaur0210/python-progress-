#print the base 10 integer denoting the maximum number of consecutive 1's in it's binary representation. 
# When working with different bases, it is common to show the base as a subscript.
n = int(input("enter any no : "))
l=[]
while(n>=1):
    d= n%2
    l.append(d)
    n=n//2
l.reverse()

print(l)    
count =1
maxc= 0
for x in range(1,len(l)):
    if(l[x-1] == l[x] and l[x]==1):
        count = count +1
    else:
        maxc = max(maxc,count)
        count = 1
print(maxc)       


        