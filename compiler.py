
# Predictive Parse Table
parse_table = {
    'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
    'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['ɛ'], '$': ['ɛ']},
    'T': {'a': ['F', 'R'], '(': ['F', 'R']},
    'R': {'+': ['ɛ'], '-': ['ɛ'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['ɛ'], '$': ['ɛ']},
    'F': {'a': ['a'], '(': ['(', 'E', ')']}
}

# parser function
def input_parser(input):
    print('Input: ' + input)
    tokens = [x for x in input] 
    stack = ['$', 'E']

    while len(stack) > 0:
        # if token is $ then end of string
        if tokens[0] == '$':
            tokens.pop(0)
            break
        top = stack.pop()
        # if top of the stack is in parse table keys
        if top in parse_table.keys():
            # if current token is in predictive parsing table
            if tokens[0] in parse_table[top].keys():
                # Identify the production
                production = parse_table[top][tokens[0]]
                for symbol in reversed(production):
                    # add production to stack in reverse order
                    if symbol != 'ɛ':
                        stack.append(symbol)
            else:
                # if current token not predictive table then its not valid
                print('Unexpected token \''+ tokens[0] + '\'')
                print('Output: String is invalid!')
                return
        # if top of the stack is same as our token, go to the next token
        elif top == tokens[0]:
            tokens.pop(0)
        # if top of the stack is not the same token and is not part of the table keys then its invalid.
        else:
            print('Unexpected token \''+ tokens[0] + '\'')
            print('Output: String is invalid!')
            return
        # Print the stack flow for each match.
        print('Stack: [', ', '.join(stack), ']')
    # if more tokens left then input is invalid    
    if len(tokens) > 0:
        print('Unexpected token \''+ tokens[0] + '\'')
        print('Output: String is invalid!')
        return
    else:
        print('Output: String is accepted.')


# test cases
input_parser('(a+a)$')
input_parser('(a+a)e$')
input_parser('(a+a)*a$')
input_parser('a*(a/a)$')
input_parser('a(a+a)$')
    
