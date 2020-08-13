'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Sort the array
    arr.sort()

    # Set up index tracker
    index = 0

    # Iterate through the integers, incrementing by 2 each time
    while(index < len(arr)):
        # If the integer at the current index is not equal to the next integer
        # That's the solution
        if arr[index] != arr[index + 1]:
            return arr[index]
        index += 2

    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")