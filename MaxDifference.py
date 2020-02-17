# a = [1, 2, 74, 100, 29, 50]

a = [500, 100, 29, 50, 1]
print(a)
maxm = a[0]
mini = a[0]

for i in range(len(a)):
    if a[i] >= maxm:
        maxm = a[i]
        max_index = i

for i in range(max_index):
    if a[i] < mini:
        mini = a[i]

print(maxm)
print(mini)

max_difference = maxm - mini
print(max_difference)
