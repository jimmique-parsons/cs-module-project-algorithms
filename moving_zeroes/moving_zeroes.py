'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # Tracker for last non zero int 
    lastNonZeroIdx = 0

    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[i], arr[lastNonZeroIdx] = arr[lastNonZeroIdx], arr[i]
            lastNonZeroIdx += 1
        print(arr)

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    moving_zeroes(arr)

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")