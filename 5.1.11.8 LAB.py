sample1= input("Write first sentence ")
sample2= input("Write seconds sentence ")
sample1 = sample1.replace(" ","")
sample2 = sample2.replace(" ","")
sample1= sample1.lower()
sample2= sample2.lower()
s1_list= list(sample1)
s2_list=list(sample2)

for letter in s1_list:
    if letter not in s2_list:
        print("not anagram")
        break
    else:
        s2_list.remove(letter)


if len(s2_list) == 0:
    print('its an anagram!')