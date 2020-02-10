
from random import randint
from random import seed
from random import randrange
from random import choice

# Python program for implementation of MergeSort 
def mergeSort(arr): 
	if len(arr) > 1: 
        #Find the midpoint of the larger array.
		mid = len(arr)//2
        #Left subarray is from index[0] to index[mid]  
		L = arr[:mid] 
        #Right subarray is from index[mid+1] to index[end]
		R = arr[mid:]

        #Call the mergeSort function recursively to split the 
        # sub arrays into smaller halves. until they have a size of 1.
		mergeSort(L)  
		mergeSort(R)  

		i = j = k = 0
		
		#Merge the subarrays into a single array. 
		while i < len(L) and j < len(R): 
            #if the left array has a smaller number at index i,
            #then it will be added to the bigger array first
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
            #If Right subarray has a smaller number,
            # then it will be added to the subarray first
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		#Check to see if any element is left in the Left half
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		#Check to see if any element is left in the Right half
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1


#Driver method
if __name__ == '__main__': 
    print("Enter the length of the array: ")
    n = int(input())

    arr = []

    min, max = map(int, input("Enter Min and Max, separated by a space:").split())
    seed(1)

    for _ in range(n):
        value = randint(min,max)
        arr.append(value)
    #print out the array selcted
    print("Your array is: " ,arr)
    mergeSort(arr)
    print("Sorted array is: ", arr)
