n = input()
listOps = []
for _ in range(int(n)):
    operation, *numbers = input().split()
    if operation == str("insert"):
        listOps.insert(int(numbers[0]), int(numbers[1]))
    elif operation == str("print"):
        print(listOps)
    elif operation == str("remove"):
        listOps.remove(int(numbers[0]))
    elif operation == str("append"):
        listOps.append(int(numbers[0]))
    elif operation == str("sort"):
        listOps.sort()
    elif operation == str("pop"):
        listOps.pop()
    elif operation == str("reverse"):
        listOps.reverse()
