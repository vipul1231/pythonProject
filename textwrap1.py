import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    list_of_wrapped_string = wrapper.wrap(string)
    return "\n".join(list_of_wrapped_string)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
