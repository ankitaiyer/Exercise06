import pprint

inputfile = open("short.txt")
filecontents = inputfile.read()

before_wordlist = filecontents.lower().split()

# Separating file into words
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
        #word_dict.setdefault(word,1)
        word_dict[word] = 1

#print "PRINTING KEYS SORTED ALPHABETICALLY"
pprint.pprint(word_dict)

resultlist = []
key_list = []

unique_value_list = list(set(word_dict.values()))
#print type(unique_value_list)
# listname1 =[]

# for key,value in word_dict.items():
#     for i in range(len(unique_value_list)):
#         print i
#         print 'unique_value_list',unique_value_list[i] 
#         if value == i:
# print listname1

word10list = []
for key, value in word_dict.iteritems():
    if value == 10:
        word10list.append(key)

word10list_sorted = sorted(word10list)
print word10list_sorted

result_dict = {}
for i in word10list_sorted:
    #result_dict[i] = word_dict[i]
    resultlist.extend([(i, word_dict[i])])

print resultlist



