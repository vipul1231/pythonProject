
input_string = str(input())
vowels = "AEIOU"
input_string_list = list(input_string)
input_string_length = len(input_string)
kevin = 0
stuart = 0
for i in range(input_string_length):
    if input_string_list[i] in vowels:
        kevin += input_string_length - i
    else:
        stuart += input_string_length - i


if kevin > stuart:
    print("Kevin "+str(kevin))
elif kevin < stuart:
    print("Stuart "+str(stuart))
else:
    print("Draw")
