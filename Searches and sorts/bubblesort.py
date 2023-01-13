def bubbleSort(arr):
    Length = len(arr)
    for i in range(Length-1):
        for j in range(0, Length-i-1):
            if arr[j] > arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
    return arr
 
 

arr = [4, 24, 45, 72, 13, 23]
 
print(bubbleSort(arr))
 
