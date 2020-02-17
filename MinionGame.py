def check_vowel(str):
    vowel_list = ["a", "e", "i", "o", "u"]
    if str[0].lower() in vowel_list:
        return True
    else:
        return False



str1 = "BANANA"

vowel_usr = []
cons_usr = []


for y in range(len(str1)):
    for x in range(len(str1)):
        if x+1+y > len(str1):
            break
        temp = str1[y:x+1+y]
        if check_vowel(temp):
            vowel_usr.append(temp)
        else:
            cons_usr.append(temp)

print(vowel_usr)
print(cons_usr)

# from collections import Counter
# score_vowel_usr = Counter(vowel_usr)
# score_cons_usr = Counter(cons_usr)

print("vowel_usr score - " + str(len(vowel_usr)))
print("cons_usr_score - " + str(len(cons_usr)))

def print_winner(str1,str2):
    if len(str1) > len(str2):
        return "STUART", len(str1)
    else:
        return "KEVIN" , len(str2)
