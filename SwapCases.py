def swap_case(s):
    inp = str(s).split()

    result = ""
    for i in range(len(inp)):
        array = inp[i]
        mapper = map(str, array)
        listArray = list(mapper)
        for j in range(len(listArray)):
            if listArray[j].isupper():
                listArray[j] = listArray[j].lower()
            elif listArray[j].islower():
                listArray[j] = listArray[j].upper()
        result = result + ''.join(listArray) + " "

    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
