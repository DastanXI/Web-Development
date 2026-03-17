MKAD_LENGTH = 109

v = int(input())
t = int(input())

distance = v * t

position = distance % MKAD_LENGTH

print(position)