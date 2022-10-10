# def pig_latin(word):
#     if word[0] in 'aeiou':
#         return f"{word}way"

#     return f"{word[1:]}{word[0]}ay"

# print(pig_latin("apple"))

# def pig_latin(a):
#     cnt = 0
#     for i in a:
#         if i in 'aeiou' :
#             cnt += 1
#         else :
#             cnt += 0
#     if cnt >= 2:
#         print(f"{a}way")        
#     else :
#         print(f"{a[1:]}{a[0]}ay")
# a = "wine"
# b = set(a)
# pig_latin(a)

# def pig_latin(a):
#     if len(c&d) >= 2 :
#         print(f"{a}way")
#     else :
#         print(f"{a[1:]}{a[0]}ay")
# a = "wine"
# b = "aeiou"
# c = set(a)
# d = set(b)
# pig_latin(a)

def pig_latin(a):
    if len(c&d) >= 2 :
        return f"{a}way"
    return f"{a[1:]}{a[0]}ay"
a = "wine"
b = "aeiou"
c = set(a)
d = set(b)
print(pig_latin(a))