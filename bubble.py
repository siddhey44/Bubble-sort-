
def bubble_sort(arr) :
    n = len (arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if (arr[j]>arr[j+1]) :
                #left is more than right ,swap 
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [23,45,54,11,9,6,59]
print(arr)
bubble_sort(arr)
print(arr)