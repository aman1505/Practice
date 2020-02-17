a = "Hello There "
b = "Hey Hi"
# Output = "H","e","He"

# a = "hi tha"
# b = "hi there"
# print(a[0:2])
# if a[1:1] in b:
#     print(a)
c = set()
final_list = []
for y in range(len(a)):
    for x in range(len(a)):
        if a[x:x+y+1] in b and a[x:x+y+1]!=" ":
            res = (a[x:x+y+1])
            if res in final_list:
                pass
            else:
                final_list.append(res)
            continue

print(final_list)

