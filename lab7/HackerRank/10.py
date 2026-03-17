lst = []
n = int(input())

for _ in range(n):
    cmd = input().split()
    action = cmd[0]

    if action == "insert":
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif action == "print":
        print(lst)
    elif action == "remove":
        lst.remove(int(cmd[1]))
    elif action == "append":
        lst.append(int(cmd[1]))
    elif action == "sort":
        lst.sort()
    elif action == "pop":
        lst.pop()
    elif action == "reverse":
        lst.reverse()