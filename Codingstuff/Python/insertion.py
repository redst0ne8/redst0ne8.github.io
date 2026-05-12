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

# Main execution function
def main():
    print("Merge-Insertion Sorter [Python]")
    array = gen_array()
    print(f"Array to sort: {array}")
    sorted = sort(array)
    print(f"Sorted Array: {sorted}")

# Runtime
main()