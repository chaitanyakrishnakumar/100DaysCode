def odd_or_even(number):
    if number % 2 == 0:  
        return "This is an even number."
    else:
        return "This is an odd number."
      
# bug is in line 2      
# bug: '=' assigns right value to left.
# fix: '==' checks if right value equals to left value.
