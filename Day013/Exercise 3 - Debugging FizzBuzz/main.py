# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# bug1 in line 4
# bug: 'or'  checks either 3 or 5, but we need both
# fix: 'and' checks both

# bug2 in line 6,8
# bug: writing multiple 'if' statements runs all of them 
# fix: 'elif' runs only where it condition is True, then exits out of loop.

# bug3 in line 11
# bug: '[]' number is being printed as list element
# fix: remove '[]'
