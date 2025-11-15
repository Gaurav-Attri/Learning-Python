def get_operands_and_operator(problem):
    additionOperator = True if problem.find('+') != -1 else False
    operands = problem.split(' + ' if additionOperator else ' - ')
    return operands, additionOperator

def contains_digits_only(problems):
    for problem in problems:
        operands = get_operands_and_operator(problem)[0]
        if not (operands[0].isdigit() and operands[1].isdigit()):
            return False
    return True

def operands_have_four_digits_only(problems):
    for problem in problems:
        operands = get_operands_and_operator(problem)[0]
        if not (len(operands[0]) <= 4 and len(operands[1]) <= 4):
            return False
    return True

def arithmetic_arranger(problems, show_answers=False):
    # Wrong Format input handling code
    if len(problems) > 5:
        return 'Error: Too many problems.'
    if len(list(filter(lambda problem: problem.find('*') != -1 or problem.find('/') != -1, problems))) != 0:
        return "Error: Operator must be '+' or '-'."
    if not contains_digits_only(problems):
        return 'Error: Numbers must only contain digits.'
    if not operands_have_four_digits_only(problems):
        return 'Error: Numbers cannot be more than four digits.'

    # Correct Format input handling code
    first_output_line = ''
    second_output_line = ''
    third_output_line = ''
    fourth_output_line = ''
    final_output = ''

    for i, problem in enumerate(problems):
        string_operands, additionOperator = get_operands_and_operator(problem)
        operands = list(map(lambda operand: int(operand), string_operands))
        result = operands[0] + operands[1] if additionOperator else operands[0] - operands[1]

        left_operand_smallest = True if len(string_operands[0]) < len(string_operands[1]) else False
        operands_len_diff = abs(len(string_operands[0]) - len(string_operands[1]))
        max_len_operand = max(len(string_operands[0]), len(string_operands[1]))

        string_operands[0] = (string_operands[0][::-1] + ' '*2)[::-1]
        # string_operands[1] = ('+ ' if additionOperator else '- ') + string_operands[1]

        if left_operand_smallest:
            string_operands[0] = (string_operands[0][::-1] + ' '*operands_len_diff)[::-1]
        else:
            string_operands[1] = (string_operands[1][::-1] + ' '*operands_len_diff)[::-1]
        
        string_operands[1] = (string_operands[1][::-1] + (' +' if additionOperator else ' -'))[::-1]

        
        separator = '    ' if i < len(problems)-1 else ''


        string_operands[0] = string_operands[0]
        string_operands[1] = string_operands[1]
        
        first_output_line += string_operands[0] + separator
        second_output_line += string_operands[1] + separator
        third_output_line += '-'*(max_len_operand+2) + separator
        fourth_output_line += (str(result)[::-1] + ' '*((max_len_operand+2)-len(str(result))))[::-1] + separator
        
    
    final_output = first_output_line + '\n' + second_output_line + '\n' + third_output_line

    if show_answers:
        final_output += '\n' + fourth_output_line

    return final_output
        



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')