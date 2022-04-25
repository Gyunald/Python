d1 = {"a":1, "b":2, "c": 3}
d2 = {"a":1, "f":2, "c": 4}

def dictdiff(first, second) :
    output = {}
    all_keys = first.keys() | second.keys()
    print(all_keys)
    for key in all_keys :
        if first.get(key) != second.get(key) :
            output[key] = [first.get(key), second.get(key)]
    return output

if __name__ == "__main__" :
    print(dictdiff(d1, d2))

# def update(d1,d2):
#     d1.update(d2)
#     d1.update(e = 5, f =6)
#     return d1
# print(update(d1,d2))