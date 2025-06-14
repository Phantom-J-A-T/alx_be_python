def safe_divide(numerator, denominator):
   try:
       result = numerator / denominator
       return result
   except ValueError:
        return "Error: Invalid input, please provide numbers."
   except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
   