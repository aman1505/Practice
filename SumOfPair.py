# initialize a dictionary with 0 for every key
#


num = [1, 2, 5, 5, 10, 6, 4]
num_dict = dict()

for i in num:
    num_dict[i] = 0

sum = 10

print("original num_dict-----\n")
print(num_dict)

for n1 in num:
    n2 = sum - n1
    if n2 in num_dict:
        num_dict[n2] = n1
    else:
        pass
print("modified num_dict----\n")
print(num_dict)

result = []

for key, value in num_dict.items():
    if value == 0:
        continue
    else:
        result.append((key, value))
print(result)
