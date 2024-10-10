# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# Question A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Question B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Question C
desired_stars = int(input("Number of stars: "))
for i in range(desired_stars):
    print("*", end='')
print()

# Question D
desired_stars = int(input("Number of stars: "))
for i in range(1, desired_stars + 1):
    print(i * "*", sep='')
print()
