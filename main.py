""" A Python program that reverses a list in fixed-size groups, flipping each chunk separately while keeping the overall group order the same."""

k = 3

arr = [1,2,3,4,5,6,7,8]

def reverseArr(arr, k):
    for i in range(0, len(arr), k):
        arr[i:i+k] = arr[i:i+k][::-1]

    return arr

print(reverseArr(arr, k))