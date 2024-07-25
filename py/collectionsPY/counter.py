from collections import Counter
a="aababbaaoidnncnndnjdjdjjjajjjc"
my_counter=Counter(a)
print(a)
print(my_counter)
print(type(my_counter))
print(my_counter.keys)
print(my_counter.most_common(1))
print(my_counter.most_common(3))
b="hello"
c="olleh"
if(Counter(b)==Counter(c)):
    print("Anagram")
else:
    print("moron")





