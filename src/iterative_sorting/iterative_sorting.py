# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for x in range (cur_index, len(arr)):
            if arr[x] < arr[cur_index]:
                smallest_index = x



        # TO-DO: swap
            j = arr[cur_index]
            arr[cur_index] = arr[smallest_index]
            arr[smallest_index] = j
        


    return arr

# print(selection_sort([9, 5, 4, 3, 2, 7, 6]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    j = len(arr) - 1

    while j != 0:
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                x = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = x

        j = j - 1

    return arr

# print(bubble_sort([9, 5, 4, 3]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr