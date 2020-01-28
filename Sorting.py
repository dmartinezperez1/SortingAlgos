
array = [1,8,4,9,2,5,3,6,7]


def bubbleSort(array): 
    #Find length of the array.
    n = len(array) 
  
    # Outer for loop, runs until all elements are sorted 
    for i in range(n): 
  
        #inner for loop the starts at index 0 and before the last elements after they have been placed in the end  
        for j in range(0, n-i-1): 
  
            #If the first element [0] is > [1], then switch places.
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 

bubbleSort(array)     
print ("Sorted array is:") 
for i in range(len(array)): 
    print ("%d" %array[i]),  