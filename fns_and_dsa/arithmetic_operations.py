def perform_operation(num1: float, num2: float, operation: str) -> float:
    match operation:
        case "add":
            return num1 + num2
        case "substract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0.0:
                print("Unable to divide by zero")
            else:
                return num1 / num2
        case _:
            print("Unknown operation")

