def extra_end(str):
    last2 = str[-2:]
    return last2 + last2 + last2

print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))