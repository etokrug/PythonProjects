"adder.py: defines an adder function according to a slightly unusual definiteion."
import numbers

def adder(x, y):
    if isinstance(x, list) and not isinstance(y, list):
        return x + [y]
    elif isinstance(y, list) and not isinstance(x, list):
        return y + [x]
    elif isinstance(x, numbers.Number) and isinstance(y, str):
        return str(x) + y
    return x+y