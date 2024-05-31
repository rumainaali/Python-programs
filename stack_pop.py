'''Date:31/05/24
Input is an array of strings of an arithmetic expression. Calculate the value.
eg - input ["1", "2", "+", "5", "*"]
output = 15
explanation (1 + 2) * 5 = 15

input ["10", "2", "3", "+","-", "5", "*"]
output = 25
explanation (10 - ( 2 + 3)) * 5 = 25
Hint : Use the concept of stack. Push and pop. 
Parse the input list one element at a time. Convert to integer, push it to a stack. Whenever you see an
operator, pop two elements from the stack, apply the operation and push the result back.
'''

def evaluate_exp(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    return stack[0]

input_tokens = ["10", "2", "3", "+", "-", "5", "*"]
result = evaluate_expression(input_tokens)
print(f"Result: {result}")
