
def calculate(formula: str, parameters):
    formula = formula.replace('PI', '3.141592653589793')
    return eval(formula, parameters)

