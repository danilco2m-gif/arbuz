def safe_calc(func):
    def wrapper(expression):
        try:
            return func(expression)
        except Exception as e:
            return f"Error: {e}"
    return wrapper

@safe_calc
def calculate(expression):
    return eval(expression)

print(calculate("2+2"))      
print(calculate("10/0"))      
print(calculate("abc")) 