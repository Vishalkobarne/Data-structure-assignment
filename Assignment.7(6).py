#Q6.Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
def postfix_to_prefix(expression):
    stack = []
    for c in expression: 
        if c.isnumeric():
            stack.append(c)

        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = c + op1 + op2
            stack.append(result)
    return stack[0]

print(postfix_to_prefix("34+5*"))  
print(postfix_to_prefix("23+45*+")) 
