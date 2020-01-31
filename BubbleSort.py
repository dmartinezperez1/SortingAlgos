from random import randint
from random import seed
from random import choice 
from random import randrange

#Input length of array
print("Enter how many numbers in array:")
n=int(input())

#define array with lenght of n.
array = []

#Get input from user of desire range.
min, max = map(int, input("Enter minimum and maximum of range(Separate by a space):").split())

#initalize random
seed(1)
#Generate the randomly selcted array
for _ in range(n):
    value = randint(min,max)
    array.append(value)
#print out the array selcted
print("Your array is: " ,array)

def bubbleSort(array): 
    #Find length of the array.
    length = len(array) 
  
    # Outer for loop, runs until all elements are sorted 
    for i in range(length): 
  
        #inner for loop the starts at index 0 and before the last elements after they have been placed in the end  
        for j in range(0, length-i-1): 
  
            #If the first element [0] is > [1], then switch places.
            if array[j] > array[j+1] : 
                array[j], array[j+1] = array[j+1], array[j] 

#Call function bubblesort.
bubbleSort(array) 
#print out sorted array.    
print ("Sorted array is:", array)
#append the new order of the array 
for i in range(len(array)):   
    array.append(array[i])
 
