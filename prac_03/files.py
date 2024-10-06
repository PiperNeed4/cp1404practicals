# 1.
out_file = open("name.txt", 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", 'r') as in_file:
    integer_1 = int(in_file.readline())
    integer_2 = int(in_file.readline())
print(integer_1 + integer_2)

# 4.
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        integer = int(line)
        total += integer
    print(total)