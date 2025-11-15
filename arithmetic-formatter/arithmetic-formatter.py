def contains_digits_only(problems):
    for problem in problems:
        additionOperator = True if problem.find('+') != -1 else False
        operands = problem.split(' + ' if additionOperator else ' - ')
        if not (operands[0].isdigit() and operands[1].isdigit()):
            return False
    return True

def operands_have_four_digits_only(problems):
    for problem in problems:
        additionOperator = True if problem.find('+') != -1 else False
        operands = problem.split(' + ' if additionOperator else ' - ')
        if not (len(operands[0]) <= 4 and len(operands[1]) <= 4):
            return False
    return True

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    if len(list(filter(lambda problem: problem.find('*') != -1 or problem.find('/') != -1, problems))) != 0:
        return "Error: Operator must be '+' or '-'."
    if not contains_digits_only(problems):
        return 'Error: Numbers must only contain digits.'
    if not operands_have_four_digits_only(problems):
        return 'Error: Numbers cannot be more than four digits.'

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')