
#list is an in-built function in python.
l1 = []

l1.append(1)
l1.append(1.5)
l1.append('python')

print(l1[0])

#we need to import array because array is not in-built function in python .
import array

arr = array.array('i',[1,2,3,4,5]) #here i meaning 'int' data type
print(arr)
arr[0] = 10
print(arr)

#help() #help function in python