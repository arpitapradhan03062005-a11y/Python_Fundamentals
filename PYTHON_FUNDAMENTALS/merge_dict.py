dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 40}

merge = {}

for key1,value1 in dict1.items():
        if key1 in dict2.keys():
            value2 = dict2.get(key1)
            merge.update({key1:value1 + value2})

        else:
              merge.update({key1:value1})

for key2,value2 in dict2.items():
      if key2 not in dict1.keys():
            merge.update({key2:value2})

print(merge)