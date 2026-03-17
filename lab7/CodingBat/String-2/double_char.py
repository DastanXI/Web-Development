def double_char(s):
    result = ""
    for i in range(len(s)):
        result += s[i] * 2
    return result

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))