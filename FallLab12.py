#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 12
# Description :prefix/postfix
# Collaborators: NONE

def preToPstMethod(input):
    """
    makes a prefix expression to postfix expression.
    
    
    """
    # Split the prefix expression
    tkn = input.split()
    # Reverse - process right to left
    tkn = tkn[::-1]
    
    # Initialize an empty stack
    stack = []
    
    # operators for arithmetic
    op = set(['+', '-', '*', '/', '^'])
    
    # Process 
    for token in tkn:
        if token in op:
            # Pop two elements
            op1 = stack.pop()
            op2 = stack.pop()
            # Form the postfix expression and push it
            new_expr = f"{op1} {op2} {token}"
            stack.append(new_expr)
        else:
            # if op --> goes into stack
            stack.append(token)
    
    
    return stack[-1]


print("Enter a prefix expression (but a space between each character - and a space after the last one):")
input = input().strip()
    
# print
ans = preToPstMethod(input)
print(f"Postfix expression: {ans}")
