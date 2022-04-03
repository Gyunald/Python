def ubbi_dubbi(word):
    li = []
    for i in word:
        if i in 'aeiou':
            li.append(f"ub{i}")
        else:
            li.append(i)
    return "".join(li)

print(ubbi_dubbi("elephant"))