# TO-DO: Complete the selection_sort() function below
def swapPositions(list, pos1, pos2): 
      
    # popping both the elements from list 
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    # inserting in each others positions 
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)   
      
    return list

def selection_sort(arr):

    if len(arr) < 2:

        return arr

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for t in range(cur_index, len(arr)):

            if arr[t] < arr[smallest_index]:

                smallest_index = t

        if cur_index == smallest_index:

            continue

        else:

            swapPositions(arr, cur_index, smallest_index) 
        

    return arr


# TO-DO:  implement the Bubble Sort function below

def swap(arr, pos):

    element = arr.pop(pos)

    arr.insert(pos + 1, element)

    return arr


def bubble_sort(arr):
    # Your code here

    if len(arr) < 2:

        return arr

    switch = True

    while switch:

        counter = 0

        for i in range(len(arr) -1):

        
            if arr[i] > arr[i + 1]:

                swap(arr, i)

                counter += 1
        
        if counter == 0:

            switch = False

    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
