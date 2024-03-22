import random
import time



#we will prove that binary search is faster than native search

#naive search : scan List and ask is that index's value equal to the target

#if target is on the List we return index otherwise we return -1
def NaiveSearch (List , target) :
    for i in range (len(List)) : 
        if List[i] == target : 
            return i
    
    return -1




#binary search : use devide and conqure

def BinarySearch(List , target , low = None , high =None) : 
   
    if low is None :
        low = 0
    if high is None : 
        high = len(List) - 1

    if high<low :
        return -1   

    MidPoint= (low+high)//2

    if List[MidPoint] == target :
        return MidPoint
    
    elif List[MidPoint] > target : 
        return BinarySearch(List , target , low , MidPoint -1)

    elif List[MidPoint] < target :
        return BinarySearch(List , target , MidPoint + 1 , high)
        
        


if __name__ == '__main__' :
    List = [23,21,1,2,3,4,6,76,23,45,8,9,0]
    target = int(input("enter the value that you are looking for: "))

    print(NaiveSearch(List , target))
    print(BinarySearch(List , target))


    #build a sorted List of length 10000
    length = 10000

    SortedList = set()

    while len(SortedList)<length :

        SortedList.add(random.randint(-3*length , 3*length))

    SortedList = sorted(list(SortedList))


    #check nave search time
    start = time.time()
    
    for target in SortedList :
        NaiveSearch(SortedList,target)

    end = time.time()

    print("Naive search time: " , (end-start)/length , "seconds")

    #check binary search time
    start = time.time()
    
    for target in SortedList :
        BinarySearch(SortedList,target)

    end = time.time()

    print("Binary search time: " , (end-start)/length , "seconds")