words = 'this is a bunch of words'.split()
# x = map(len, words)
# print(sum(x))

def a(one_word):
    return len(one_word) > 4

x = filter(a, words)
print(",".join(x))