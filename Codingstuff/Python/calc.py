num_a = input("Enter the first number: ")
num_b = input("Enter the second number: ") 
try:
    num_a = float(num_a)
    num_b = float(num_b)
    
    sum_result = num_a + num_b
    diff_result = num_a - num_b
    prod_result = num_a * num_b
    if num_b != 0:
        quot_result = num_a / num_b
    else:
        quot_result = "undefined (division by zero)"
    
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {prod_result}")
    print(f"Quotient: {quot_result}")
finally:    print("Calculation complete.")