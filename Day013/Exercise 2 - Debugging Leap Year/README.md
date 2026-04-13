# Instructions

- Read the code given below,
- Spot the problems 🐞,
- Modify the code to fix the program.

# code
```python
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```        
