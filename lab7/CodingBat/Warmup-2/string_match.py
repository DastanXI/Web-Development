def string_match(a, b):
    length = min(len(a), len(b))
    count = 0

    for i in range(length - 1):
        if a[i:i + 2] == b[i:i + 2]:
            count += 1
    return count

print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))