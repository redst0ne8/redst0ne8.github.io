import random as rng
import datetime as dt
import json
now = dt.datetime.now()

def login():
    user = input("What is your username?\n")
    password = input("What is your password?\n")
    print(f"\nLogging in, {user}...")
    if (user == "redst0ne8" and password == "yourmom"):
        return True
    else: return False

def fetch_rector_state():
    data = {"name": "Alice", "scores": [88, 92, 79], "active": True}

    # Write JSON
    with open("reactor.json", "w") as f:
        json.dump(data, f, indent=4)   # indent= makes it human-readable

    # Read JSON
    with open("reactor.json", "r") as f:
        loaded = json.load(f)
    print("Loaded JSON:", loaded)
    print("Name:", loaded["name"])
    return

def main():
    authenticated = login()
    if not authenticated: return print("Invalid credentials. Please try again.")
    elif authenticated: 
        print("Authenticated.\n")
        print(f"The date is: {now.strftime("%A, %B %d %Y")}\nFetching reactor status...")
        print("[REACTOR_NODE_4+]: init MAIN...")
        fetch_rector_state()

main()