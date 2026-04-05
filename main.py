# =============================================================================
# PYTHON COMPREHENSIVE REFERENCE — All Major Day-to-Day Topics
# =============================================================================
# Run any section by calling its function at the bottom of the file.
# Each section is self-contained and heavily commented.
# =============================================================================


# =============================================================================
# 1. VARIABLES & DATA TYPES
# =============================================================================
def variables_and_types():
    print("\n" + "="*60)
    print("1. VARIABLES & DATA TYPES")
    print("="*60)

    # --- Basic types ---
    my_int       = 42               # Integer
    my_float     = 3.14             # Float (decimal)
    my_string    = "Hello, World"   # String
    my_bool      = True             # Boolean: True or False
    my_none      = None             # None = absence of value

    print(f"int:    {my_int}   → type: {type(my_int)}")
    print(f"float:  {my_float} → type: {type(my_float)}")
    print(f"str:    {my_string} → type: {type(my_string)}")
    print(f"bool:   {my_bool}  → type: {type(my_bool)}")
    print(f"None:   {my_none}  → type: {type(my_none)}")

    # --- Type conversion (casting) ---
    print("\n--- Type Conversion ---")
    print(int("99"))        # String → int:   99
    print(float("3.5"))     # String → float: 3.5
    print(str(100))         # Int    → string: "100"
    print(bool(0))          # 0, "", None, [] = False; everything else = True
    print(bool("hello"))    # Non-empty string = True

    # --- Checking type ---
    print("\n--- isinstance() checks ---")
    print(isinstance(42, int))          # True
    print(isinstance("hi", str))        # True
    print(isinstance(3.14, (int, float)))  # True — checks against multiple types


# =============================================================================
# 2. NUMBERS & MATHS
# =============================================================================
def numbers_and_maths():
    print("\n" + "="*60)
    print("2. NUMBERS & MATHS")
    print("="*60)

    # --- Operators ---
    print(10 + 3)   # Addition:       13
    print(10 - 3)   # Subtraction:    7
    print(10 * 3)   # Multiplication: 30
    print(10 / 3)   # Division:       3.333... (always float)
    print(10 // 3)  # Floor division: 3        (rounds down)
    print(10 % 3)   # Modulo:         1        (remainder)
    print(10 ** 3)  # Exponent:       1000     (10 to the power of 3)

    # --- Augmented assignment (shorthand) ---
    x = 10
    x += 5   # same as x = x + 5  → 15
    x -= 3   # same as x = x - 3  → 12
    x *= 2   # same as x = x * 2  → 24
    x //= 5  # same as x = x // 5 → 4
    print(f"After augmented ops: {x}")

    # --- Built-in math functions ---
    print(abs(-7))          # Absolute value:  7
    print(round(3.7))       # Round:           4
    print(round(3.1415, 2)) # Round to 2 dp:   3.14
    print(min(4, 7, 1, 9))  # Minimum:         1
    print(max(4, 7, 1, 9))  # Maximum:         9
    print(sum([1, 2, 3, 4]))# Sum of iterable: 10

    # --- math module (import for more power) ---
    import math
    print(math.sqrt(16))     # Square root:  4.0
    print(math.pi)           # Pi:           3.14159...
    print(math.ceil(3.2))    # Ceiling:      4
    print(math.floor(3.9))   # Floor:        3
    print(math.log(100, 10)) # Log base 10:  2.0


# =============================================================================
# 3. STRINGS — IN DEPTH
# =============================================================================
def strings_in_depth():
    print("\n" + "="*60)
    print("3. STRINGS — IN DEPTH")
    print("="*60)

    s = "  Hello, Python World!  "

    # --- Common string methods ---
    print(s.strip())            # Remove leading/trailing whitespace
    print(s.lower())            # Lowercase
    print(s.upper())            # Uppercase
    print(s.title())            # Title Case
    print(s.replace("Python", "Beautiful"))  # Replace substring
    print(s.strip().split(", "))# Split into list by delimiter
    print(s.strip().startswith("Hello"))     # True
    print(s.strip().endswith("!"))           # True
    print(s.count("l"))         # Count occurrences: 3
    print(s.find("Python"))     # Index of first match: 9 (or -1 if not found)
    print(s.strip().index("W")) # Like find() but raises error if not found
    print("  ".join(["a", "b", "c"]))  # Join list into string: "a  b  c"

    # --- Slicing strings [start:stop:step] ---
    print("\n--- Slicing ---")
    t = "Hello, World"
    print(t[0])       # First char:       H
    print(t[-1])      # Last char:        d
    print(t[0:5])     # Characters 0–4:   Hello
    print(t[7:])      # From index 7 on:  World
    print(t[:5])      # Up to index 5:    Hello
    print(t[::2])     # Every 2nd char:   Hlo ol
    print(t[::-1])    # Reversed:         dlroW ,olleH

    # --- f-strings (formatted string literals) ---
    print("\n--- f-strings ---")
    name = "Alice"
    age = 30
    pi = 3.14159
    print(f"Name: {name}, Age: {age}")
    print(f"Pi to 2dp: {pi:.2f}")           # Format float
    print(f"Padded: {name:<10}|")           # Left align, width 10
    print(f"Padded: {name:>10}|")           # Right align, width 10
    print(f"Int:    {1000000:,}")           # Thousands separator: 1,000,000

    # --- Multi-line strings ---
    multi = """
    Line 1
    Line 2
    Line 3
    """
    print(multi)

    # --- Raw strings (useful for file paths and regex) ---
    path = r"C:\Users\name\Documents"   # r"" ignores escape characters
    print(path)


# =============================================================================
# 4. LISTS
# =============================================================================
def lists_in_depth():
    print("\n" + "="*60)
    print("4. LISTS")
    print("="*60)

    fruits = ["apple", "banana", "cherry", "date", "elderberry"]

    # --- Accessing ---
    print(fruits[0])        # First:  apple
    print(fruits[-1])       # Last:   elderberry
    print(fruits[1:3])      # Slice:  ['banana', 'cherry']

    # --- Modifying ---
    fruits.append("fig")            # Add to end
    fruits.insert(1, "avocado")     # Insert at index 1
    fruits[0] = "APPLE"             # Replace by index
    fruits.extend(["grape", "kiwi"])# Add multiple items
    print(fruits)

    # --- Removing ---
    fruits.remove("date")   # Remove first occurrence by value
    popped = fruits.pop()   # Remove & return last item
    popped2 = fruits.pop(1) # Remove & return item at index 1
    print(f"Popped: {popped}, {popped2}")
    del fruits[0]           # Delete by index (no return)
    print(fruits)

    # --- Searching & info ---
    nums = [3, 1, 4, 1, 5, 9, 2, 6]
    print(len(nums))            # Length:                8
    print(nums.count(1))        # Count of value 1:      2
    print(nums.index(5))        # Index of value 5:      4
    print(5 in nums)            # Membership check:      True

    # --- Sorting ---
    print(sorted(nums))             # Returns NEW sorted list (ascending)
    print(sorted(nums, reverse=True))  # Descending
    nums.sort()                     # Sorts IN PLACE (modifies original)
    nums.reverse()                  # Reverses IN PLACE
    print(nums)

    words = ["banana", "apple", "cherry"]
    words.sort(key=len)         # Sort by length
    print(words)
    words.sort(key=lambda w: w[-1])  # Sort by last letter
    print(words)

    # --- List comprehensions (powerful one-liner loops) ---
    print("\n--- List Comprehensions ---")
    squares = [x**2 for x in range(1, 6)]
    print(squares)                               # [1, 4, 9, 16, 25]

    evens = [x for x in range(20) if x % 2 == 0]
    print(evens)                                 # [0, 2, 4, 6, ...]

    upper_fruits = [f.upper() for f in ["apple", "banana"]]
    print(upper_fruits)                          # ['APPLE', 'BANANA']

    # --- Unpacking ---
    a, b, c = [10, 20, 30]
    print(a, b, c)

    first, *rest = [1, 2, 3, 4, 5]
    print(first, rest)   # 1  [2, 3, 4, 5]

    # --- Copying lists (IMPORTANT — avoids mutation bugs) ---
    original = [1, 2, 3]
    bad_copy = original         # This is NOT a copy — same object!
    good_copy = original.copy() # This IS a copy
    good_copy2 = original[:]    # Also a copy
    bad_copy.append(99)
    print("Original after bad_copy mutated:", original)  # [1, 2, 3, 99] ← affected!
    good_copy.append(88)
    print("Original after good_copy mutated:", original) # unchanged ✓


# =============================================================================
# 5. TUPLES & SETS
# =============================================================================
def tuples_and_sets():
    print("\n" + "="*60)
    print("5. TUPLES & SETS")
    print("="*60)

    # --- Tuples: ordered, IMMUTABLE (can't change after creation) ---
    # Use when data shouldn't change: coordinates, RGB values, DB rows, etc.
    print("--- Tuples ---")
    point = (10, 20)
    rgb = (255, 128, 0)
    single = (42,)          # Note the comma — (42) is just an int!

    print(point[0])         # Access by index: 10
    x, y = point            # Unpack into variables
    print(f"x={x}, y={y}")

    # Tuples support most list read-operations
    print(len(rgb))
    print(rgb.count(255))
    print(rgb.index(128))
    print(255 in rgb)

    # --- Sets: unordered, NO DUPLICATES, fast membership testing ---
    print("\n--- Sets ---")
    s = {1, 2, 3, 3, 2, 1}
    print(s)                    # {1, 2, 3} — duplicates removed!

    s.add(4)                    # Add item
    s.discard(2)                # Remove (no error if missing)
    s.remove(1)                 # Remove (raises error if missing)
    print(s)

    # Set operations (great for comparing groups)
    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7}
    print(a | b)    # Union:        {1,2,3,4,5,6,7} — all items
    print(a & b)    # Intersection: {3,4,5}         — shared items
    print(a - b)    # Difference:   {1,2}            — in a but not b
    print(a ^ b)    # Symmetric diff:{1,2,6,7}       — in one but not both

    print(3 in a)   # Fast membership check — better than list for large data


# =============================================================================
# 6. DICTIONARIES
# =============================================================================
def dictionaries_in_depth():
    print("\n" + "="*60)
    print("6. DICTIONARIES")
    print("="*60)

    # Dictionaries: key-value pairs, ordered (Python 3.7+), mutable
    person = {
        "name": "Alice",
        "age": 30,
        "city": "London",
        "hobbies": ["reading", "hiking"]
    }

    # --- Accessing ---
    print(person["name"])               # Direct access (KeyError if missing)
    print(person.get("age"))            # Safe access (returns None if missing)
    print(person.get("salary", 0))      # Safe access with default value: 0

    # --- Modifying ---
    person["age"] = 31                  # Update existing key
    person["email"] = "a@example.com"  # Add new key
    del person["city"]                  # Delete a key
    removed = person.pop("email")       # Delete & return value
    print(f"Removed: {removed}")

    # --- Iterating ---
    print("\n--- Iterating ---")
    for key in person:                  # Iterate keys
        print(key)

    for key, value in person.items():   # Iterate key-value pairs
        print(f"  {key}: {value}")

    print(list(person.keys()))          # All keys as a list
    print(list(person.values()))        # All values as a list

    # --- Checking & merging ---
    print("name" in person)            # Check key exists: True
    person.update({"age": 32, "country": "UK"})  # Merge another dict
    print(person)

    # --- Nested dictionaries ---
    print("\n--- Nested Dict ---")
    users = {
        "user1": {"name": "Bob", "score": 95},
        "user2": {"name": "Carol", "score": 88},
    }
    print(users["user1"]["name"])       # Bob
    print(users["user2"]["score"])      # 88

    # --- Dictionary comprehension ---
    squares = {x: x**2 for x in range(1, 6)}
    print(squares)   # {1:1, 2:4, 3:9, 4:16, 5:25}

    # Filter a dict
    high_scores = {k: v for k, v in {"a": 80, "b": 55, "c": 90}.items() if v >= 80}
    print(high_scores)


# =============================================================================
# 7. CONTROL FLOW — IF / ELIF / ELSE
# =============================================================================
def control_flow():
    print("\n" + "="*60)
    print("7. CONTROL FLOW")
    print("="*60)

    # --- if / elif / else ---
    score = 72

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score {score} → Grade: {grade}")

    # --- Ternary (one-line if/else) ---
    status = "pass" if score >= 50 else "fail"
    print(f"Status: {status}")

    # --- Comparison operators ---
    print(5 == 5)    # Equal
    print(5 != 4)    # Not equal
    print(5 > 3)     # Greater than
    print(5 >= 5)    # Greater than or equal
    print(3 < 5)     # Less than
    print(3 <= 3)    # Less than or equal

    # --- Logical operators ---
    x = 7
    print(x > 5 and x < 10)    # AND: both must be True → True
    print(x < 5 or x > 6)      # OR:  at least one True → True
    print(not x > 5)            # NOT: inverts → False

    # --- Identity & membership ---
    a = None
    print(a is None)            # is: checks identity (use for None checks)
    print(a is not None)
    print("e" in "hello")       # in: membership
    print(3 not in [1, 2, 4])   # not in

    # --- match/case (Python 3.10+ switch equivalent) ---
    command = "quit"
    match command:
        case "start":
            print("Starting...")
        case "stop" | "quit":   # Multiple values with |
            print("Stopping.")
        case _:                 # Default case
            print("Unknown command.")


# =============================================================================
# 8. LOOPS
# =============================================================================
def loops_in_depth():
    print("\n" + "="*60)
    print("8. LOOPS")
    print("="*60)

    # --- for loop ---
    for i in range(5):          # 0, 1, 2, 3, 4
        print(i, end=" ")
    print()

    for i in range(2, 10, 2):   # Start=2, Stop=10, Step=2 → 2 4 6 8
        print(i, end=" ")
    print()

    # --- Looping over collections ---
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    # --- enumerate() — get index AND value ---
    for i, fruit in enumerate(fruits):
        print(f"  {i}: {fruit}")

    for i, fruit in enumerate(fruits, start=1):  # Start index at 1
        print(f"  {i}. {fruit}")

    # --- zip() — loop multiple lists together ---
    names = ["Alice", "Bob", "Carol"]
    scores = [88, 92, 79]
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")

    # --- while loop ---
    print("\n--- while loop ---")
    count = 0
    while count < 5:
        print(count, end=" ")
        count += 1
    print()

    # --- break, continue, else ---
    print("\n--- break / continue / else ---")
    for n in range(10):
        if n == 3:
            continue        # Skip this iteration
        if n == 7:
            break           # Exit loop entirely
        print(n, end=" ")
    print()

    # Loop else: runs only if loop completed WITHOUT a break
    for n in range(5):
        if n == 10:
            break
    else:
        print("Loop finished naturally (no break hit)")

    # --- Nested loops ---
    print("\n--- Nested loops ---")
    for row in range(1, 4):
        for col in range(1, 4):
            print(f"({row},{col})", end=" ")
        print()


# =============================================================================
# 9. FUNCTIONS — IN DEPTH
# =============================================================================
def functions_in_depth():
    print("\n" + "="*60)
    print("9. FUNCTIONS — IN DEPTH")
    print("="*60)

    # --- Basic function ---
    def greet(name):
        return f"Hello, {name}!"
    print(greet("Alice"))

    # --- Default parameter values ---
    def greet2(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    print(greet2("Bob"))
    print(greet2("Bob", "Good morning"))

    # --- *args: variable number of positional arguments (tuple) ---
    def add_all(*numbers):
        return sum(numbers)
    print(add_all(1, 2, 3, 4, 5))  # 15

    # --- **kwargs: variable keyword arguments (dict) ---
    def print_info(**details):
        for k, v in details.items():
            print(f"  {k}: {v}")
    print_info(name="Alice", age=30, city="London")

    # --- Multiple return values (returns a tuple) ---
    def min_max(numbers):
        return min(numbers), max(numbers)
    low, high = min_max([3, 1, 7, 2, 9])
    print(f"Min: {low}, Max: {high}")

    # --- Lambda (anonymous one-liner functions) ---
    print("\n--- Lambda ---")
    square = lambda x: x ** 2
    print(square(5))   # 25

    # Lambdas shine as inline keys for sort/filter/map
    names = ["Charlie", "Alice", "Bob"]
    names.sort(key=lambda n: len(n))   # Sort by name length
    print(names)

    # --- map(), filter(), sorted() with lambdas ---
    nums = [1, 2, 3, 4, 5, 6]
    doubled   = list(map(lambda x: x * 2, nums))      # Apply func to each
    evens     = list(filter(lambda x: x % 2 == 0, nums))  # Keep if True
    print(f"Doubled: {doubled}")
    print(f"Evens:   {evens}")

    # --- Scope: local vs global ---
    print("\n--- Scope ---")
    total = 100     # Global variable

    def update_total():
        global total         # Declare we're modifying the global
        total += 50

    update_total()
    print(f"Global total: {total}")   # 150

    # --- Docstrings (document your functions!) ---
    def divide(a, b):
        """
        Divides a by b.

        Args:
            a (float): Numerator
            b (float): Denominator (must not be zero)

        Returns:
            float: Result of a / b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    print(divide(10, 3))
    print(divide.__doc__)  # Print the docstring


# =============================================================================
# 10. ERROR HANDLING (TRY / EXCEPT)
# =============================================================================
def error_handling():
    print("\n" + "="*60)
    print("10. ERROR HANDLING")
    print("="*60)

    # --- Basic try/except ---
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    # --- Multiple except blocks ---
    def safe_convert(value, to_type):
        try:
            return to_type(value)
        except ValueError:
            print(f"ValueError: Cannot convert '{value}' to {to_type.__name__}")
        except TypeError:
            print(f"TypeError: Invalid type provided")
        return None

    print(safe_convert("abc", int))   # ValueError
    print(safe_convert("42", int))    # 42

    # --- except Exception as e: catch the error object ---
    try:
        my_list = [1, 2, 3]
        print(my_list[10])
    except IndexError as e:
        print(f"Caught IndexError: {e}")

    # --- else: runs if NO exception occurred ---
    # --- finally: ALWAYS runs (great for cleanup) ---
    try:
        x = int("99")
    except ValueError:
        print("Conversion failed")
    else:
        print(f"Conversion succeeded: {x}")
    finally:
        print("This always runs (e.g., close a file/DB connection here)")

    # --- Raising exceptions manually ---
    def set_age(age):
        if not isinstance(age, int):
            raise TypeError("Age must be an integer.")
        if age < 0 or age > 150:
            raise ValueError(f"Age {age} is out of valid range.")
        return age

    try:
        set_age(-5)
    except ValueError as e:
        print(f"Caught: {e}")

    # --- Common built-in exceptions to know ---
    # ValueError      — right type, wrong value
    # TypeError       — wrong type entirely
    # KeyError        — dict key doesn't exist
    # IndexError      — list index out of range
    # AttributeError  — object doesn't have that attribute
    # FileNotFoundError — file doesn't exist
    # ZeroDivisionError — divide by zero
    # ImportError     — module not found
    # NameError       — variable not defined


# =============================================================================
# 11. FILE I/O
# =============================================================================
def file_io():
    print("\n" + "="*60)
    print("11. FILE I/O")
    print("="*60)

    filename = "example.txt"

    # --- Writing a file ---
    # "w" = write (creates or overwrites)
    # "a" = append (adds to existing)
    # Always use 'with' — it auto-closes the file even if an error occurs
    with open(filename, "w") as f:
        f.write("Line 1: Hello\n")
        f.write("Line 2: World\n")
        f.writelines(["Line 3: Python\n", "Line 4: Files\n"])
    print(f"Written to {filename}")

    # --- Reading a file ---
    # "r" = read (default)
    with open(filename, "r") as f:
        content = f.read()          # Read entire file as one string
    print("Full content:\n", content)

    with open(filename, "r") as f:
        lines = f.readlines()       # Read into list of lines (with \n)
    print("As list:", lines)

    with open(filename, "r") as f:
        for line in f:              # Memory-efficient line-by-line reading
            print(line.strip())

    # --- Appending to a file ---
    with open(filename, "a") as f:
        f.write("Line 5: Appended!\n")

    # --- Checking if file exists before opening ---
    import os
    if os.path.exists(filename):
        print(f"{filename} exists")

    # --- Working with file paths (os.path) ---
    print(os.path.abspath(filename))        # Full absolute path
    print(os.path.basename("/some/path/file.txt"))  # file.txt
    print(os.path.dirname("/some/path/file.txt"))   # /some/path
    print(os.path.splitext("report.pdf"))   # ('report', '.pdf')
    print(os.path.join("folder", "sub", "file.txt"))  # folder/sub/file.txt

    # --- Working with JSON files (very common!) ---
    import json
    data = {"name": "Alice", "scores": [88, 92, 79], "active": True}

    # Write JSON
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)   # indent= makes it human-readable

    # Read JSON
    with open("data.json", "r") as f:
        loaded = json.load(f)
    print("Loaded JSON:", loaded)
    print("Name:", loaded["name"])

    # Convert to/from JSON string (without files)
    json_string = json.dumps(data)       # dict → JSON string
    back_to_dict = json.loads(json_string)  # JSON string → dict
    print(json_string)

    # Cleanup temp files
    for temp_file in [filename, "data.json"]:
        if os.path.exists(temp_file):
            os.remove(temp_file)


# =============================================================================
# 12. CLASSES & OBJECT-ORIENTED PROGRAMMING (OOP)
# =============================================================================
def oop_basics():
    print("\n" + "="*60)
    print("12. OOP — CLASSES")
    print("="*60)

    # A class is a blueprint for creating objects
    class Animal:
        # Class variable — shared across ALL instances
        kingdom = "Animalia"

        # __init__ is the constructor — runs when object is created
        def __init__(self, name, species, age):
            # Instance variables — unique to each object
            self.name = name
            self.species = species
            self.age = age

        # Instance method — acts on this specific object
        def speak(self):
            return f"{self.name} makes a sound."

        def birthday(self):
            self.age += 1
            return f"{self.name} is now {self.age}!"

        # __str__ defines what print(object) shows
        def __str__(self):
            return f"{self.name} ({self.species}), age {self.age}"

        # __repr__ is for developers/debugging
        def __repr__(self):
            return f"Animal(name={self.name!r}, species={self.species!r}, age={self.age})"

    # Creating instances
    cat = Animal("Whiskers", "Cat", 3)
    dog = Animal("Rex", "Dog", 5)

    print(cat)              # Uses __str__
    print(repr(dog))        # Uses __repr__
    print(cat.speak())
    print(dog.birthday())
    print(Animal.kingdom)   # Class variable

    # --- Inheritance: child class extends a parent class ---
    print("\n--- Inheritance ---")
    class Dog(Animal):
        def __init__(self, name, age, breed):
            super().__init__(name, "Dog", age)  # Call parent's __init__
            self.breed = breed

        # Override parent method
        def speak(self):
            return f"{self.name} says: Woof!"

        def fetch(self, item):
            return f"{self.name} fetched the {item}!"

    fido = Dog("Fido", 4, "Labrador")
    print(fido)
    print(fido.speak())         # Uses Dog's speak()
    print(fido.birthday())      # Uses Animal's birthday()
    print(fido.fetch("ball"))

    print(isinstance(fido, Dog))     # True
    print(isinstance(fido, Animal))  # True — it IS an Animal too


# =============================================================================
# 13. MODULES & IMPORTS
# =============================================================================
def modules_and_imports():
    print("\n" + "="*60)
    print("13. MODULES & IMPORTS")
    print("="*60)

    # Import a whole module
    import math
    print(math.sqrt(25))

    # Import specific items (no need to prefix with module name)
    from math import sqrt, pi, factorial
    print(sqrt(36))
    print(pi)
    print(factorial(5))

    # Import with alias (shorter name)
    import datetime as dt
    import random as rng

    # --- datetime: working with dates and times ---
    print("\n--- datetime ---")
    now = dt.datetime.now()
    print(now)                          # Current date and time
    print(now.year, now.month, now.day)
    print(now.strftime("%Y-%m-%d %H:%M"))  # Format as string
    print(now.strftime("%A, %B %d %Y"))    # e.g. "Sunday, April 06 2025"

    today = dt.date.today()
    print(today)

    birthday = dt.date(1995, 6, 15)
    delta = today - birthday
    print(f"Days since birthday: {delta.days}")

    # Add/subtract time
    tomorrow = now + dt.timedelta(days=1)
    last_week = now - dt.timedelta(weeks=1)
    print(f"Tomorrow: {tomorrow.date()}")
    print(f"Last week: {last_week.date()}")

    # --- random: generating random numbers ---
    print("\n--- random ---")
    print(rng.randint(1, 10))           # Random int between 1 and 10 inclusive
    print(rng.random())                 # Random float between 0.0 and 1.0
    print(rng.uniform(1.5, 5.5))       # Random float in range
    items = ["apple", "banana", "cherry"]
    print(rng.choice(items))            # Random item from list
    rng.shuffle(items)                  # Shuffle list IN PLACE
    print(items)
    print(rng.sample(range(100), 5))   # 5 unique random numbers from range

    # --- os: operating system interactions ---
    print("\n--- os ---")
    import os
    print(os.getcwd())                  # Current working directory
    print(os.listdir("."))              # List files in current dir
    os.makedirs("temp_folder", exist_ok=True)  # Create directory (no error if exists)
    os.rmdir("temp_folder")            # Remove empty directory
    print(os.environ.get("HOME", "Not found"))  # Read environment variable

    # --- sys ---
    import sys
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    # sys.exit(0) — exit the script (0 = success, 1 = error)


# =============================================================================
# 14. COMPREHENSIONS — ALL TYPES
# =============================================================================
def comprehensions():
    print("\n" + "="*60)
    print("14. COMPREHENSIONS")
    print("="*60)

    # List comprehension: [expression for item in iterable if condition]
    squares = [x**2 for x in range(1, 11)]
    print("Squares:", squares)

    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print("Even squares:", even_squares)

    # Dict comprehension: {key: value for ...}
    word_lengths = {word: len(word) for word in ["hello", "world", "python"]}
    print("Word lengths:", word_lengths)

    # Set comprehension: {expression for ...} — no duplicates
    unique_mods = {x % 5 for x in range(20)}
    print("Unique mods:", unique_mods)

    # Generator expression: like list comp but lazy (memory efficient)
    # Use when you only need to iterate once and the list could be huge
    gen = (x**2 for x in range(1_000_000))  # Doesn't compute until used
    print("First from generator:", next(gen))
    print("Sum of first 10:", sum(x**2 for x in range(10)))

    # Nested list comprehension (2D)
    matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
    for row in matrix:
        print(row)


# =============================================================================
# 15. USEFUL BUILT-IN FUNCTIONS
# =============================================================================
def builtins_reference():
    print("\n" + "="*60)
    print("15. BUILT-IN FUNCTIONS")
    print("="*60)

    data = [3, 1, 4, 1, 5, 9, 2, 6]

    # Aggregation
    print(len(data))             # Length:         8
    print(sum(data))             # Sum:            31
    print(min(data))             # Minimum:        1
    print(max(data))             # Maximum:        9

    # Type checks / conversions (covered earlier but listing here)
    print(type(42))              # <class 'int'>
    print(isinstance(42, int))   # True

    # Iteration utilities
    print(list(range(5)))                # [0,1,2,3,4]
    print(list(enumerate(["a","b"])))    # [(0,'a'),(1,'b')]
    print(list(zip([1,2],[3,4])))        # [(1,3),(2,4)]
    print(sorted(data))                  # Sorted copy
    print(list(reversed(data)))          # Reversed copy (reversed() is a generator)

    # any() / all()
    nums = [2, 4, 6, 7, 8]
    print(any(x % 2 != 0 for x in nums))   # True — at least one odd
    print(all(x > 0 for x in nums))         # True — all positive

    # abs, round, pow, divmod
    print(abs(-7))           # 7
    print(round(3.567, 2))  # 3.57
    print(pow(2, 10))        # 1024
    print(divmod(17, 5))     # (3, 2) — quotient and remainder together

    # Input/output
    # input("Prompt: ")       # Always returns a STRING — cast it!
    print(repr("hello\nworld"))  # Show escape chars literally: 'hello\nworld'

    # dir() — see all attributes/methods of an object
    print([m for m in dir([]) if not m.startswith("_")])

    # help() — inline documentation (great in the REPL)
    # help(str.split)


# =============================================================================
# 16. STRING FORMATTING METHODS (BONUS)
# =============================================================================
def string_formatting():
    print("\n" + "="*60)
    print("16. STRING FORMATTING (EXTRA)")
    print("="*60)

    # f-string (preferred — Python 3.6+)
    name, value = "Alice", 3.14159
    print(f"Name: {name}, Value: {value:.2f}")

    # .format() method (older but still common)
    print("Name: {}, Value: {:.2f}".format(name, value))
    print("Name: {n}, Value: {v:.2f}".format(n=name, v=value))

    # % formatting (legacy — you'll see it in older code)
    print("Name: %s, Value: %.2f" % (name, value))

    # Formatting numbers
    big = 1234567.891
    print(f"{big:,.2f}")         # 1,234,567.89  — comma separator
    print(f"{big:>20.2f}")       # Right-aligned in 20 chars
    print(f"{0.001234:.2e}")     # Scientific notation: 1.23e-03
    print(f"{255:b}")            # Binary:  11111111
    print(f"{255:x}")            # Hex:     ff
    print(f"{255:o}")            # Octal:   377

    # String padding/alignment
    print(f"{'left':<15}|")      # Left-aligned
    print(f"{'right':>15}|")     # Right-aligned
    print(f"{'center':^15}|")    # Centered
    print(f"{'padded':*^15}|")   # Centered, padded with *


# =============================================================================
# MAIN — Run all sections
# =============================================================================
def main():
    variables_and_types()
    numbers_and_maths()
    strings_in_depth()
    lists_in_depth()
    tuples_and_sets()
    dictionaries_in_depth()
    control_flow()
    loops_in_depth()
    functions_in_depth()
    error_handling()
    file_io()
    oop_basics()
    modules_and_imports()
    comprehensions()
    builtins_reference()
    string_formatting()

main()