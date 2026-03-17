def same_first_last(a):
    return len(a) >= 1 and a[0] == a[len(a) - 1]

print(same_first_last('Deep sea'))
print(same_first_last('David'))