def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
            continue

        if s[i] in '()*+':
            tokens.append(s[i])
            i += 1

        elif s[i] == '-':
            is_unary = (not tokens or (isinstance(tokens[-1], str) and tokens[-1] in '+-*(' or
               (i > 0 and s[i-1] == ' ' and (not tokens or str(tokens[-1]) in '+-*('))))
            if is_unary:
                i += 1
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i < len(s) and s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    tokens.append(-num)
                elif i < len(s) and s[i] == '(':
                    tokens.extend([-1, '*', '('])
                    i += 1
                elif i < len(s) and s[i] == '-':
                    continue
                else:
                    return None
            else:
                tokens.append('-')
                i += 1

        elif s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            tokens.append(num)

        else:
            return None
    return tokens


def to_polish_notation(tokens):
    output = []
    operators = []
    priority = {'+': 1, '-': 1, '*': 2}

    for token in tokens:
        if isinstance(token, int):
            output.append(token)

        elif token in '+-*':
            while (operators and operators[-1] != '(' and
                   priority[operators[-1]] >= priority[token]):
                output.append(operators.pop())
            operators.append(token)

        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators or operators[-1] != '(':
                return None
            operators.pop()

    while operators:
        if operators[-1] == '(':
            return None
        output.append(operators.pop())

    return output


def solve_rpn(rpn):
    if rpn is None:
        return None

    stack = []
    for token in rpn:
        if isinstance(token, int):
            stack.append(token)
        elif token in '+-*':
            if len(stack) < 2:
                return None
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    return stack[0] if len(stack) == 1 else None


s = input().strip()
if not s:
    print('WRONG')
else:
    tokens = tokenize(s)
    if tokens is not None:
        rpn = to_polish_notation(tokens)
        result = solve_rpn(rpn)
        print(result if result is not None else 'WRONG')
    else:
        print('WRONG')
