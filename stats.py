# calculate and print the respective mean, median, and mode on separate lines. 
# If your array contains more than one modal value, choose the numerically smallest one.
if __name__ == '__main__':
    n = int(input("enter the no of elemnts in an array : ").strip())

    arr = list(map(int, input().rstrip().split()))
summ = 0
n= len(arr)
for i in range(n):
        summ = summ +arr[i]

mean = round((summ/n),2)    
print(mean)    

arr2 = sorted(arr)        
if(n%2==1):
       median = arr2[round((n//2)-1)]     
elif(n%2==0):
    #print(arr2[round(n/2)],arr2[round((n//2)-1)])
    median = (arr2[round(n/2)] + arr2[round((n//2)-1)] )/2

print(round(median,2)) 
count ={}
for i in arr:
    if(i in count):
        count[i]=+1
    else:
        count[i] = 1

lar  = max(count.values())
mode=[]
for key, value in count.items():
    if (value == lar):
        mode.append(key)

print(min(mode))

from scipy import stats 
mode = stats.mode(arr)
print(mode)