def check_parentheses(string):
    stack = []
    result = [' '] * len(string)
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                result[i] = '?'
        else:
            result[i] = ' '

    for idx in stack:
        result[idx] = 'x'

    return ''.join(result)

def process_multiple_lines(lines):
    for line in lines:
        line = line.rstrip()
        marks = check_parentheses(line)
        print(line)
        print(marks)

if __name__ == "__main__":
    lines = []
    try:
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
    except EOFError:
        pass

    process_multiple_lines(lines)
