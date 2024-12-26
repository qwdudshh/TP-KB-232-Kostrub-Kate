act = ["(", "+", "-", "*", "/", "^", ")"]

def priority(action):
    match act.index(action):
        case 0:
            return 0  
        case 1 | 2:
            return 1  
        case 3 | 4:
            return 2  
        case 5:
            return 3  

def infix_to_rpn(expression):
    exp_elem = expression.split()  
    stack = []
    output = []

    for elem in exp_elem:
        if elem in act:  
            if elem == act[0]:  
                stack.append(elem)
            elif elem == act[6]: 
                while stack[-1] != act[0]: 
                    output.append(stack.pop())
                stack.pop()  
            else:  
                while stack and priority(stack[-1]) >= priority(elem):
                    output.append(stack.pop())
                stack.append(elem)
        else:
            output.append(elem)  

    while stack:  
        output.append(stack.pop())

    return output

def evaluate_rpn(rpn):
    stack = []

    for elem in rpn:
        if elem in act:  # Оператор
            b = float(stack.pop())
            a = float(stack.pop())
            match elem:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case "/":
                    stack.append(a / b)
                case "^":
                    stack.append(a ** b)
        else:
            stack.append(elem)  

    return stack[0]

if __name__ == "__main__":
    expression = input("Enter your expression (use spaces between numbers and operators): ")
    print(f"Original expression: {expression}")

    rpn = infix_to_rpn(expression)
    rpn_str = " ".join(rpn)
    print(f"Reverse Polish notation: {rpn_str}")

    result = evaluate_rpn(rpn)
    print(f"Result: {result}")
