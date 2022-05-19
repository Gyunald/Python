import random

def creat_password_generator(password):
    def creat_password(length):
        output = []
        for i in range(length):
            output.append(random.choice(password))
        return "".join(output)
    return creat_password

a = creat_password_generator("abcdef")
print(a(5))