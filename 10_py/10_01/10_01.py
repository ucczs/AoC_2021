with open('input.txt') as f:
    lines = f.readlines()

openCharsColl = ['(', '[', '{', '<']
matchingChars = {'(': ')', '[': ']', '{': '}', '<': '>'}

counting = {')': 3, ']': 57, '}': 1197, '>': 25137}

result = 0
for line in lines:
    openChar = []
    closingChar = []
    chars = list(line.strip())
    for c in chars:
        if c in openCharsColl:
            openChar.append(c)
        else:
            if matchingChars[openChar[-1]] == c:
                del openChar[-1]
            else:
                result += counting[c]
                break

print(result)
