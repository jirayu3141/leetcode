def findMedian(arr):
    # sort the array
    arr.sort()

    # find the median
    if len(arr) % 2 == 0:
        # if the length of the array is even
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2
    else:
        # if the length of the array is odd
        return arr[len(arr) // 2]

if __name__ == '__main__':
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    result = findMedian(arr)
    
    print(result)