# Calculator
def calculate(n1,n2):
    calc_added = n1 + n2
    calc_subtracted = n1 - n2
    calc_multiplied = n1 * n2
    calc_float_divided = n1 / n2
    calc_floor_divided = n1 // n2
    calc_remainder = n1 % n2
    print(f"""\nTOTAL CALCULATION RESULTS:
          Numbers: {n1}, {n2};
          Addition: {calc_added};
          Subtraction: {calc_subtracted};
          Multiplication: {calc_multiplied};
          Division:
          [FLOAT]: {calc_float_divided} | [FLOOR]: {calc_floor_divided} | [REMAINEDER]: {calc_remainder}""")
    return

# Manipulating strings
def string_manipulation():
    print("\nSTRING MANIPULATION")
    print(r"\n","\tMakes a new line.")
    print(r"\t","\tEnters an indent.")
    print(r"\ ","\tUsed as an escape character.") # \"
    return

def concatenation(str1, str2, list):
    final_list = list.split(",")
    print("\nCONCATENAION")
    print("String Basic combination:\n",str1 + str2)
    print("Multiplicity of a string:\n",(str1 * 3) + (str2 * 2))
    print(f"""Word Indexing
          String 1:
            Length: {len(str1)}
            Pos 1: {str1[0]}
          String 2:
            Length: {len(str2)}
            Pos 1: {str2[0]}
          """)
    print("Lists length:",len(final_list))
    print("List indexing: First Pos:",final_list[0])
    print("List indexing: Final Pos:",final_list[-1])
    return

# Runtime functionality
def main():
    # Define an array of options and print the intro and list of options
    options = ["calculate", "string_manipulation", "concatenation"]
    print("Welcome to example python project.\nAvailable programs:",options)

    # Request the function to run and run case match.
    func = input("Which function do you want to run?\n")
    match func:
        case "calculate":
            # For calculator case, first get inputs and sanity check input types for int.
            input_n1 = int(input("What is the first number?\n" ))
            input_n2 = int(input("What is the second number?\n" ))
            if not (input_n1 and input_n2):
                return print("You did not input one or more numbers.\nPlease re-run the script to try again") 
            else: return calculate(input_n1, input_n2)
        case "string_manipulation":
            return string_manipulation()
        case "concatenation":
            input_str1 = str(input("What is the first string?\n"))
            input_str2 = str(input("What is the second string?\n"))
            input_list = input("Please input a list of numbers separated by only commas. [,]\n")
            if not (input_str1 and input_str2 and input_list):
                return print("You did not input one or more strings.\nPlease re-run the script to try again") 
            else: return concatenation(input_str1, input_str2, input_list)
        case _:
            # Exit script if no valid function passed
            return print("That is not a function.\nPlease re-run the script")

main()