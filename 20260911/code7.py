#sum of digits of a number

def sum_of_digits(number):
    number = abs(int(number))
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(num))
