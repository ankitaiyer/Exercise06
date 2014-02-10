
import pprint

inputfile = open("medium.txt")
filecontents = inputfile.read()

before_wordlist = filecontents.lower().split()

wordlist = []
for word in before_wordlist:
    newword = word.strip(",.:?!#*()[]%@$^&")
    wordlist.append(newword)



word_dict = {}

#go thru wordlist, if increment the value if the word exists,
#else if word is not in the dict, add it as a key, default value of 1

for word in wordlist:
    if word in word_dict:
        word_dict[word]+= 1
    else:
        word_dict.setdefault(word,1)

# prints output alphabetically
print "PRINTING KEYS SORTED ALPHABETICALLY"
pprint.pprint(word_dict)

word_dict_sorted_keys = sorted(word_dict, key=word_dict.get)

print "PRINTING KEYS SORTED BY VALUE (LOW TO HIGH)"
for item in word_dict_sorted_keys:
    print item, word_dict[item]


