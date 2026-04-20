def calculator(a: float, b: float, operacja: str="/") -> float:
    if operacja == "+":
        return a + b
    elif operacja == "-":
        return a - b
    elif operacja == "*":
        return a *b
    elif operacja == "/":
        if b == 0:
            return None
        return a / b
    
print(calculator(10, 20, "+"))