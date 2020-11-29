
from collections import Counter

no_shoes = int(input())
list_of_shoes = list(input().split(" "))
map_of_shoes = Counter(list_of_shoes)
customers = int(input())
earning =0
for i in range(customers):
    size, dollar = map(int, input().split(" "))
    if map_of_shoes.get(str(size)) is not None and map_of_shoes.get(str(size)) != 0:
        earning += dollar
        list_of_shoes.remove(str(size))
        map_of_shoes = Counter(list_of_shoes)

print(earning)
print(map_of_shoes)