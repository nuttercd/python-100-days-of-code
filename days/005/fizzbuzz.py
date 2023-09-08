# If a number is divisible by 3 then print "Fizz"
# If the number is divisible by 5 then print "Buzz"
# If it is both print Fizz Buzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)