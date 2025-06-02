from random import randint

attempts = 0
max_attempts = 5

while True:
    if attempts == max_attempts:
        print("\nYou lose! You are out of attempts\n")
        break

    else:

        try:
            user_input = int(input("\nEnter a number from 1 to 10: "))

        except ValueError:
            print("\nEnter a numeric value!")
            continue

        computer = randint(1, 10)
        attempts += 1

        if not 1 <= user_input <= 10:
            print("\nPlease choose a number from 1 to 10!")
            continue

        else:

            if user_input == computer:
                print(f"\nYou won the game in {attempts} attempt(s)!\n")
                break

            else:
                print(f"\nTry again! You have {max_attempts-attempts} attempt(s) left")