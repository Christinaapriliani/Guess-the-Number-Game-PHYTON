import random

def main():
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("Guess the Number Game")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
