# -*- coding: utf-8 -*-
"""bubble_sort.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jGPJ0SM8bShCIvmYZiL0-GmRSRLisScY
"""



"""# bubble sort"""

my_array=[64, 34, 25, 12, 22, 11, 90, 5]

n=len(my_array) #length of an array or get the number of elements in the array, here n=8
print("length of my_array is: ", n)
print("-----------------------------")
#outer loop controls the number of passes through the list
#outer loop for each pass
for i in range(n-1): # we need n-1 passes
  #we need n-1 passes always (for i ranging from 0 to n-2) because after n-1 passes, the list will be sorted.
  #here, i (index)= n-1
  #on each pass, the largest unsorted element "bubbles up" to its correct position at the end of the unsorted part of the array.
  print("just checking the value of i= ", i)
  print("just checking the value of n-1= ", n-1, "n-1 is 7 because it starts from 0")
  print("-----------------------------")

  #inner loop to perform comparisons and swaps for this pass
  #inner loop goes through the unsorted part of the aary and perform comparisons and swaps.
  for j in range(n-i-1): #j starts from 0 and goes up to n-i-2. This range decreases by one with each outer loop pass (i). This is because, after each pass, the largest element among the unsorted elements is placed at the end, so it does not need to be checked again.
    print("j=", j)
    print("-----------------------------")
    if my_array[j]>my_array[j+1]:#swap if the left element if greater than the right element in list of array #checks if current element if greater than the next element?
      my_array[j], my_array[j+1]=my_array[j+1],my_array[j] #if current elemnet is greater than the next elemnet, the two elemnets are swapped.
print("sorted_array is: ", my_array)

'''
Step-by-Step Execution Example:
my_array = [64, 34, 25, 12, 22, 11, 90, 5].
n = 8.


Pass 1 (i = 0)
The largest element should bubble to the end.

Compare 64 and 34: swap → [34, 64, 25, 12, 22, 11, 90, 5]
Compare 64 and 25: swap → [34, 25, 64, 12, 22, 11, 90, 5]
Compare 64 and 12: swap → [34, 25, 12, 64, 22, 11, 90, 5]
Compare 64 and 22: swap → [34, 25, 12, 22, 64, 11, 90, 5]
Compare 64 and 11: swap → [34, 25, 12, 22, 11, 64, 90, 5]
Compare 64 and 90: no swap
Compare 90 and 5: swap → [34, 25, 12, 22, 11, 64, 5, 90]
After Pass 1, the largest element 90 is in its correct position.

Pass 2 (i = 1)
The second largest element should bubble to the second last position.

Compare 34 and 25: swap → [25, 34, 12, 22, 11, 64, 5, 90]
Compare 34 and 12: swap → [25, 12, 34, 22, 11, 64, 5, 90]
Compare 34 and 22: swap → [25, 12, 22, 34, 11, 64, 5, 90]
Compare 34 and 11: swap → [25, 12, 22, 11, 34, 64, 5, 90]
Compare 34 and 64: no swap
Compare 64 and 5: swap → [25, 12, 22, 11, 34, 5, 64, 90]
After Pass 2, 64 is in its correct position.

Pass 3 (i = 2)
The third largest element should bubble to the third last position.

Compare 25 and 12: swap → [12, 25, 22, 11, 34, 5, 64, 90]
Compare 25 and 22: swap → [12, 22, 25, 11, 34, 5, 64, 90]
Compare 25 and 11: swap → [12, 22, 11, 25, 34, 5, 64, 90]
Compare 25 and 34: no swap
Compare 34 and 5: swap → [12, 22, 11, 25, 5, 34, 64, 90]
After Pass 3, 34 is in its correct position.

Subsequent Passes
The process continues similarly, with each pass moving the next largest unsorted element into its correct position. The remaining passes proceed until all elements are sorted.

Final Sorted Array
After all passes, the sorted array is:

c
Copy code
Sorted array: [5, 11, 12, 22, 25, 34, 64, 90]
Summary
Outer Loop: Controls the number of passes (total of n-1 passes).
Inner Loop: Compares and swaps adjacent elements, reducing the range in each pass.
Swapping Condition: Moves larger elements to the right, gradually sorting the array from largest to smallest elements in each pass.





'''

