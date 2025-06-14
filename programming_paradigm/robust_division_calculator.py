def safe_divide(numerator, denominator):
   try:
       result = float(numerator) / float(denominator)
       return result
   except ValueError:
        return "Error: Invalid input, please provide numbers."
   except ZeroDivisionError:
        return "Error: Cannot divide by zero."
   