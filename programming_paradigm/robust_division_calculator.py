def safe_divide(numerator, denominator):
    try:
        try:
            numerator = float(numerator)
            denominator = float(denominator)
            answer = numerator / denominator
            return f"The result of the division is {answer}"
        except ValueError:
            return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
