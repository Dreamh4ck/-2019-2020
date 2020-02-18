def multiplication_addition(number):
    return number * 3 + 1

def digits_summary(number):
    sum = 0
    while number > 0:
        last_digit = number % 10
        sum += last_digit
        number = int(number/10)
    return sum

def digits_count(number):
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count

number = int(input("Enter a number:" ))
number = multiplication_addition(number)
number = digits_summary(number)
digits = digits_count(number)
if digits == 1:
    print("After the calculations the new number is: ", number)

while digits > 1:
    number = multiplication_addition(number)
    number = digits_summary(number)
    digits = digits_count(number)
    if digits == 1:
        print("After the calculations the new number is: ", number)



