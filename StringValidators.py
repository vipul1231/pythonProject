import re


def stringTest(opr_type, content):
    input_string = str(content)
    input_type = str(opr_type)
    if input_type == "alnum":
        alphabet = False
        numeric = False
        input_string_list = list(input_string)
        for i in range(len(input_string_list)):
            if str(input_string_list[i]).isnumeric():
                numeric = True
            elif str(input_string_list[i]).isalpha():
                alphabet = True
        if numeric or alphabet:
            return True
        return False
    elif input_type == "isalpha":
        alphabet = False
        input_string_list = list(input_string)
        for i in range(len(input_string_list)):
            if str(input_string_list[i]).isalpha():
                alphabet = True
                break
        if alphabet:
            return True
        return False
    elif input_type == "isdigit":
        input_string_list = list(input_string)
        for i in range(len(input_string_list)):
            if str(input_string_list[i]).isdigit():
                return True
        return False
    elif input_type == "islower":
        input_string_list = list(input_string)
        for i in range(len(input_string_list)):
            if str(input_string_list[i]).islower():
                return True
        return False
    elif input_type == "isupper":
        input_string_list = list(input_string)
        for i in range(len(input_string_list)):
            if str(input_string_list[i]).isupper():
                return True
        return False


if __name__ == '__main__':
    s = input()
    input_s = str(s)
    print(stringTest("alnum", input_s))
    print(stringTest("isalpha", input_s))
    print(stringTest("isdigit", input_s))
    print(stringTest("islower", input_s))
    print(stringTest("isupper", input_s))
