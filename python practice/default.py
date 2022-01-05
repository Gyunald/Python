def print_a_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)

        print()

print_a_times('hi','bye','again', n=3)