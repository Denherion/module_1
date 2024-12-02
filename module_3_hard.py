data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def res_calculate_structure(data_structure):
    result_ = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            result_ += res_calculate_structure(key)
            result_ += res_calculate_structure(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            result_ += res_calculate_structure(item)
    elif isinstance(data_structure, (int, float)):
        result_ += data_structure
    elif isinstance(data_structure, str):
        result_ += len(data_structure)
    return result_
result = res_calculate_structure(data_structure)
print(result)