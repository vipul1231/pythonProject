from itertools import product

list_a = input().split(" ")
list_b = input().split(" ")

A = [list_a, list_b]

A_List = list(product(*A))

for i in range(len(A_List)):
    print("("+str(A_List[i][0])+", "+str(A_List[i][1])+")", end=" ")

# print(list(product([1, 2, 3], [2, 3])))
