# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0 and number % 5 != 0:
            print("Fizz")
        if number % 5 == 0 and number % 3 != 0:
            print("Buzz")
        elif number % 3 != 0 and number % 5 != 0:
            print([number])

fizz_buzz(10)