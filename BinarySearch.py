lists = [10,20,30,40,50,60,70,80,90]
search = int(input("Enter the search element"))
def binarysearch(lists,low,high,search):
    
    if high >= low:
        mid = int((high+low)/2)
        if lists[mid]==search:
            return mid
        elif lists[mid] > search:
            return binarysearch(lists,low,mid-1,search)
        else :
            return binarysearch(lists,mid+1,high,search)
    return -1

low = 0
high = len(lists)-1
print(binarysearch(lists,low,high,search))


====================================================================


lists = [10,20,30,40,50,60,70,80,90]
search = int(input("Enter the search element"))
def binarysearch(lists,search):
    low = 0
    high = len(lists)-1
    
    while low <= high:
        mid = int((high+low)/2)
        if lists[mid] < search:
            low = mid + 1
        elif lists[mid] > search:
            high = mid-1
        else:
            return mid
        
    return -1

result = binarysearch(lists,search)
print(result)


=====================================================================


