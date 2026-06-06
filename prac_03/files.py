# 1

name = input("Enter name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
out_file.close()

# 3
with open("numbers.txt", "r") as in_file:
    number_1 = int(in_file.readline())
    number_2 = int(in_file.readline())
    total = number_1 + number_2
    print(total)

