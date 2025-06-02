from random import randint

win = 0
lose = 0
tie = 0

while True:
    try:
        user_input = int(input("\nRock(1), Paper(2), Scissor(3), Quit(4): "))

    except ValueError:
        print("\nPlease enter a numeric value!")

    if user_input == 4:
        print("\nYou are exiting the game!\n")

        print(f"win(s):{win} \nlose(s):{lose} \ntie(s):{tie}\n")
        break

    computer = randint(1, 3)

    if computer == user_input:
        print("\nIt's a tie!")
        tie += 1

    elif computer == 1 and user_input == 2:
        print("\ncomputer choose Rock. You won!")
        win += 1

    elif computer == 2 and user_input == 3:
        print("\ncomputer choose Paper. You won!")
        win += 1

    elif computer == 3 and user_input == 1:
        print("\ncomputer choose Scissor. You won!")
        win += 1

    elif computer == 2 and user_input == 1:
        print("\ncomputer choose Paper. You lose!")
        lose += 1

    elif computer == 3 and user_input == 2:
        print("\ncomputer choose Scissor. You lose!")
        lose += 1

    elif computer == 1 and user_input == 3:
        print("\ncomputer choose Rock. You lose!")
        lose += 1

    else:
        print("\nChoose from the given the option!")