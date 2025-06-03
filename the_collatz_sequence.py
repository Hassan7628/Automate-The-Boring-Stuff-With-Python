print("\n\n")


def collatz(number: int):
    if number % 2 == 0:
        result = number // 2

    else:
        result = 3 * number + 1

    print(result)
    return result


try:
    user_input = int(input("Enter a number: "))

except ValueError:
    print("\nEnter a numeric value!")

print()

if user_input == 1:
    print(user_input)

else:

    try:
        while True:
            if user_input == 1:
                break

            user_input = collatz(user_input)
            continue

    except NameError:
        pass

print("\n\n")