# Calculator
def calculate(n1,n2):
    calc_added = n1 + n2
    calc_subtracted = n1 - n2
    calc_multiplied = n1 * n2
    calc_float_divided = n1 / n2
    calc_floor_divided = n1 // n2
    calc_remainder = n1 % n2
    print(f"""TOTAL CALCULATION RESULTS:
          Numbers: {n1}, {n2};
          Addition: {calc_added};
          Subtraction: {calc_subtracted};
          Multiplication: {calc_multiplied};
          Division:
          [FLOAT]: {calc_float_divided} | [FLOOR]: {calc_floor_divided} | [REMAINEDER]: {calc_remainder}""")



# Runtime functionality
def main():
    # Define an array of options and print the intro and list of options
    options = ["calculate"]
    print("Welcome to example python project.\nAvailable programs:",options)

    # Request the function to run and run case match.
    func = input("Which function do you want to run? ")
    match func:
        case "calculate":
            # For calculator case, first get inputs and sanity check input types for int.
            input_n1 = int(input("What is the first number?" ))
            input_n2 = int(input("What is the second number?" ))
            if not (input_n1 and input_n2):
                return print("You did not input one or more numbers.\nPlease re-run the script to try again") 
            else: return calculate(input_n1, input_n2)
        case _:
            # Exit script if no valid function passed
            return print("That is not a function.\nPlease re-run the script")

main()