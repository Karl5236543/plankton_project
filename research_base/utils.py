
def calculate(formula: str, parameters):
    formula = formula.replace('PI', '3.141592653589793')
    return eval(formula, parameters)

class Cells_type_data:
    def __init__(self, type_name, cell_count, type_id):
        self.type_name = type_name
        self.cell_count = cell_count
        self.type_id = type_id