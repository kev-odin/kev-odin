# Kevin Chung
# TCSS 502 Assignment 1 - Armstrong Number Calculator (1.5 hours)
# Calculates Armstrong numbers within a use specified integer range and prints out the results.

# Obtain User Input
def get_user_input():
    print("Welcome to this Armstrong Number Calculator.")
    while True:
        try:
            integer = int(input("Please enter an integer from 10 through 100,000,000 (without the commas): "))
            if 10 <= integer <= 100_000_000:
                return integer
            else:
                print("Sorry, that value is out of the specified bounds.")
        except ValueError:
            print("This is not a valid integer. Try again and enter a whole number.")


# Calculate Armstrong Numbers
def calculate_armstrong_numbers(number):
    armstrong_count = 0
    i = 10
    print("The Armstrong numbers from 10 through " + str(number) + " are: \n")
    for i in range(i, number + 1):  # repeats n times
        if i == armstrong_sum(i):
            armstrong_count += 1
            print(i)

    print("\nThe total number of Armstrong numbers found was " + str(armstrong_count))


# Calculate the length of the user number input, better implementation
def number_length(number):
    return len(str(number))  # repeats 1 time


# Calculate the length of the user number input, first implementation
def number_length2(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count


# Calculate the Armstrong total of a number
def armstrong_sum(number):
    exponent = number_length(number)
    armstrong_total = 0

    while number > 0:  # repeats m times
        digit = number % 10
        number //= 10
        armstrong_total += pow(digit, exponent)
    return armstrong_total


# Armstrong Calculator Program
possible_armstrong = get_user_input()
calculate_armstrong_numbers(possible_armstrong)
