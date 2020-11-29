def count_substring(string, sub_string):
    sub_string_list = list(sub_string)
    stringList = list(string)
    counter = 0
    flag = False

    if len(stringList) == 1 and len(sub_string_list) == 1 and stringList[0] == sub_string_list[0]:
        return 1

    for i in range(len(stringList)):
        if stringList[i] == sub_string_list[0] and i < len(stringList)-1:
            k = i + 1
            for j in range(1, len(sub_string_list)):
                if k < len(stringList) - 1 and sub_string_list[j] == stringList[k]:
                    k = k + 1
                    flag = True
                    continue
                else:
                    flag = False
                    break
            if flag is True:
                counter = counter + 1
                flag = False
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
