import itertools

operators = '-~'


alphabet = '012345'

expression_map = {}


for i in range(15):
    for op in itertools.product(operators, repeat=i):
        for num in alphabet:
            expression = ''.join(op) + num
            result = eval(expression)
            if result not in expression_map:
                expression_map[result] = expression

for key in sorted(expression_map):
    print(f'{key}: {expression_map[key]}')




# len(f'FL4G[{expression}]') > 14
