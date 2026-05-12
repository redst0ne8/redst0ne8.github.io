# IMPORTS
import random
import math

# Make a function to generate a random array of {n} numbers from 1 to {lim}
def gen_array():
    n = input("How many numbers do you want to sort? ")
    lim = input("Starting at 1, what is the upper limit that the data can reach? (Highest number) ")
    if not n or not lim: return print("Error: You did not input a one of the two values.")
    arr = []
    for _ in range(int(n)):
        arr.append(random.randint(1, int(lim)))
    return arr

# Helper function to cut provided array {arr} in half
def split_array(arr):
    if not arr: return print("Error: No array was provided.")
    if (len(arr) % 2 == 0):
        middle = (len(arr) // 2)
    if not (len(arr) % 2 == 0):
        middle = len(arr) // 2 + 1

    left = arr[:middle]
    right = arr[middle:]
    return left, right

# Function to sort
def sort(arr):
    if not arr: 
        print("Error: No array was provided.")
        return arr
        
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

# Merge function
def merge(arr1, arr2):
    total_length = len(arr1) + len(arr2)
    result = []
    for i in range(total_length):
        i = i - 1
        if arr1[i] < arr2[i]:
            result.append(arr1[i])
        if arr1[i] > arr2[i]:
            result.append(arr2[i])
        if arr1[i] == arr2[i]:
            result.append(arr1[i])
            result.append(arr2[i])
    return result

# Main execution function
def main():
    print("Merge-Insertion Sorter [Python]")
    array = gen_array()
    print(f"Array to sort: {array}")
    array_left = split_array(array)[0]
    array_right = split_array(array)[1]
    print(f"Left Section: {array_left}, Right Section: {array_right}")
    sorted_array_left = sort(array_left)
    sorted_array_right = sort(array_right)
    print(f"Sorted Left: {sorted_array_left}, Sorted Right: {sorted_array_right}")

# Runtime
main()