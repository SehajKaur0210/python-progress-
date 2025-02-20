# find 3 quartiles 


def quartiles(arr):
    arr.sort()
    n = len(arr)
    mid = n//2
    if(n%2==0):
        lower_l = arr[:mid]
        upper_l = arr[mid:]
    else:
        lower_l = arr[:mid]
        upper_l = arr[(mid+1):]  
    
    def median(arrs):
        p = len(arrs)    
        if(p%2 ==1):
            return arrs[p//2]
        else:
            return ((arrs[p//2]+ arrs[(p//2)-1])/2)
            
    q1 = median(lower_l)
    medians = median(arr)
    q3 = median(upper_l)         
             
    print(round(q1))    
    print(round(medians))  
    print(round(q3)) 