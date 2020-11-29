import os


def solve(s):
    input_list = s.split(" ")
    for i in range(len(input_list)):
        input_list_content = list(input_list[i])
        if len(input_list_content) != 0:
            input_list_content[0] = input_list_content[0].upper()
            input_list[i] = "".join(input_list_content)
    return " ".join(input_list)


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)