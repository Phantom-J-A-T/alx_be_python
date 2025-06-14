def safe_divide(numerator, denominator):
   try:
       result = float(numerator) / float(denominator)
       return print(f"The result of the division is {result:.2f}")
   except ValueError:
        return "Error: Please enter numeric values only."
   except ZeroDivisionError:
        return "Error: Cannot divide by zero."
   