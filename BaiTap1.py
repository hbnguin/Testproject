import math

def sort(list):
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if(list[i]>list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

def binsearch(list, value):
    newlist = sort(list)
    start = 0                
    end = len(newlist)-1
    while start <= end:
        mid = math.floor((start + end)/2)
        if(newlist[mid] == value):
            return mid #return mid
        elif(value>newlist[mid]):
            start = mid + 1
        else:
            end = mid - 1
    return -1

newList = [3 , 4 , 2 , 8 , 1 , 2 , 4 , 9]
print(binsearch(newList,4))