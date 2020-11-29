inp = input()


class my_dictionary(dict):

    def __init__(self):
        super().__init__()

    def __add__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return self.__getitem__(key)

    def updatedict(self, key, value):
        self[key] = value

    def isValuePresent(self, value):
        result = self.get(value, "empty")
        if result == "empty":
            return False
        else:
            return True

    def iterate(self):
        k = 0
        for key in sorted(self.items(), key=lambda kv: (-kv[1], kv[0]), reverse=False):
            print(key[0]+" "+str(key[1]))
            k = k + 1
            if k == 3:
                break


dic_obj = my_dictionary()

for i in range(len(list(inp))):
    if not dic_obj.isValuePresent(inp[i]):
        dic_obj.__add__(inp[i], 1)
    else:
        value = dic_obj.getValue(inp[i])
        dic_obj.updatedict(inp[i], value + 1)

dic_obj.iterate()
