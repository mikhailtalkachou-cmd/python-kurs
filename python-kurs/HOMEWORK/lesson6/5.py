def calculator(a: float | int, b: float | int, operacja: str) -> float:
    """Funkcija pobera dwie zmienne i znak dzialania.
    W zaleznosci od dzialania funkcja uzywa +, -, *, /.
    A w przypadku dzelenia na 0 zwraca None"""
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