numbers = [4,5,8,1,9,12,15,999999,3,10,11] #the list that we are sorting
for a in range(1,len(numbers)): #for loop for a that will start with the "second" index because the first one is "sorted" to the last index
    key = numbers[a] #key = pivot, [] will make it an actual number in the list
    j=a-1 #j is the index that we are comparing to (to the left of a)

    while j>= 0 and numbers[j] > key: #j>=0 makes sure that this loop does not go on infinetely, the value of j has to be bigger than key, if not, the pivot role is given to the next index in the list
        numbers[j+1] = numbers[j] # shift the bigger number one position to the right
        j-=1 # move j one step to the left to continue comparing
    numbers[j+1]=key # place key (pivot) in its correct position in the sorted part of the list
print("sorted list:", numbers)   