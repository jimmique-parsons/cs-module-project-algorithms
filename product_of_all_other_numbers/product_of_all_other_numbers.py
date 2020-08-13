'''
Input: a List of integers
Returns: a List of integers
'''

def product_of_all_other_numbers(arr):
    # Set up an array to return
    products = [1] * len(arr)
    
    product_so_far = 1
    # Find the product of the numbers below the current index
    products_below = [1] * len(arr)
    for i in range(len(arr)):
        products_below[i] = product_so_far
        product_so_far *= arr[i]

    # Find the product of the numbers above the current index
    product_so_far = 1
    products_above = [1] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        products_above[i] = product_so_far
        product_so_far *= arr[i]

    # Set the product of the current index to
    #(product of numbers below that index) * (product of numbers above that index)
    for i in range(len(arr)):
        products[i] = products_below[i] * products_above[i]

    return products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")