def count_code(s):
    count = 0
    for i in range(len(s) - 3):
        if s[i:i+2] == "co" and s[i+3] == "e":
            count += 1
    return count

# Test examples
print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))