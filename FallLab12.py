#Name: Alice Mungamuri
# KUID: 3117704
# Lab Session Monday 8am
#LAB Assignment 06
# Description :prefix/postfix
# Collaborators: NONE

def prefix_to_postfix(prefix_expr):
    """
    Convert a prefix expression to postfix expression.
    
    :param prefix_expr: str, a prefix expression with variables and operators
    :return: str, equivalent postfix expression
    """
    # Split the prefix expression into tokens
    tokens = prefix_expr.split()
    # Reverse the tokens to process from right to left
    tokens = tokens[::-1]
    
    # Initialize an empty stack
    stack = []
    
    # Operators for arithmetic
    operators = set(['+', '-', '*', '/', '^'])
    
    # Process each token
    for token in tokens:
        if token in operators:
            # Pop two elements from the stack for the operator
            operand1 = stack.pop()
            operand2 = stack.pop()
            # Form the postfix expression and push it back
            new_expr = f"{operand1} {operand2} {token}"
            stack.append(new_expr)
        else:
            # If the token is an operand, push it onto the stack
            stack.append(token)
    
    # The final result will be on the top of the stack
    return stack[-1]


# Main program to take user input
if __name__ == "__main__":
    print("Enter a prefix expression (e.g., '^ - x y 2'):")
    prefix_expr = input().strip()
    
    # Convert to postfix and print the result
    postfix_expr = prefix_to_postfix(prefix_expr)
    print(f"Postfix expression: {postfix_expr}")