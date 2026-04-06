import random

def main():
    num_to_guess = random.randint(1, 100)
    guessed_correctly = False
    attempts = 0

    print('Welcome to the number guessing game!')

    while not guessed_correctly and attempts < 10:
        user_input = input('Enter your guess: ')
        attempts += 1

        if user_input.isdigit():
            guessed_num = int(user_input)
            
            if guessed_num == num_to_guess:
                print('Congratulations! You guessed the number!')
                guessed_correctly = True
            else:
                distance = abs(num_to_guess - guessed_num)
                if guessed_num < num_to_guess:
                    suffix = ", but you are very close!" if distance <= 10 else "."
                    print(f'Your guess is too low{suffix}')
                else:
                    suffix = ", but you are very close!" if distance <= 10 else "."
                    print(f'Your guess is too high{suffix}')
        else:
            print("Please enter a valid number.")

    if attempts == 10 and not guessed_correctly:
        print(f'Sorry, you have used all your attempts. The number was {num_to_guess}.')

if __name__ == "__main__":
    main()