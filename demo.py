def calculate_operation(op, x, y):
    """
    This function takes two arguments x and y and returns the result of the operation
    """
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y
    elif op == 'mul':
        return x * y
    elif op == 'div':
        return x / y
    else:
        return 'Invalid operation'
    

def main():
    print(calculate_operation('add', 2, 3))
    print(calculate_operation('sub', 2, 3))
    print(calculate_operation('mul', 2, 3))
    print(calculate_operation('div', 2, 3))
    print(calculate_operation('mod', 2, 3))


if __name__ == '__main__':
    main()
    