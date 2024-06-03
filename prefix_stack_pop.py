'''Date:3/05/2024
Same as above, but the operator come first.
eg - input ["+","1", "2", "*", "5"]
output = 15
explanation (1 + 2) * 5 = 15
input ["-","10", "+", "2", "3", "*", "5"]
output = 25
explanation (10 - ( 2 + 3)) * 5 = 25
'''

def evaluate_prefix_expression(elements):
    stack = []
    for element in reversed(elements):
        if element.isdigit():
            stack.append(int(element))
        else:
            a = stack.pop()
            b = stack.pop()
            if element == '+':
                stack.append(a + b)
            elif element == '-':
                stack.append(a - b)
            elif element == '*':
                stack.append(a * b)
    return stack[0]

elements = ["*", "-", "10", "+", "2", "3", "5"]
result = evaluate_prefix_expression(elements)
print(f"Result: {result}")
