def flatten(a):
    return sorted([int(j) for i in a for j in i if str(j).isdigit() and int(j) % 2 == 1])

if __name__ == "__main__":
    print(flatten([[1,2,"11","10","a"],[3,4,2.4,2.3,7]]))

