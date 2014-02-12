import pprint
from sys import argv

script, filename = argv

inputfile = open(filename)
filecontents = inputfile.read()

# Separating file into words
before_wordlist = filecontents.lower().split()

# Striping special characters from the words
wordlist = []
for word in before_wordlist:
    newword = word.strip(",.:?!#*()[]%@$^&")
    wordlist.append(newword)

#Create a new dict to count - number of times each word appear in the list.
word_dict = {}

#go thru wordlist, increment the counter value if the word exists,
#else if word is not in the dict, add it as a key, default value of 1

for word in wordlist:
    if word in word_dict:
        word_dict[word]+= 1
    else:
        #word_dict.setdefault(word,1)
        word_dict[word] = 1

#PPrint sorts the dict alphabetically and prints the same 
print "-------------------------------------"
print "ORIGNAL WORDS LIST = " , word_dict 
print "-------------------------------------"
print "PRINTING KEYS SORTED ALPHABETICALLY"
print "-------------------------------------"
pprint.pprint(word_dict)
print "-------------------------------------"
print "-------------------------------------"


#Print words sorted by their frequency High to low in the list
word_dict_keys_sorted_by_value = sorted(word_dict, key=word_dict.get, reverse=True)
print "PRINTING KEYS SORTED BY THEIR FREQUENCY - HIGH-TO_LOW in the file"
print word_dict_keys_sorted_by_value
print "-------------------------------------"


# Create new dict twith Key=Frequency of words e.g 5 times, 
# and Value= List of all the words that appear 5 times
swapped_word_dict = {}
for key, value in word_dict.items():
    if value not in swapped_word_dict.keys():
        swapped_word_dict[value] = [key]
    else:
        swapped_word_dict[value].append(key)  

print "After sorting Alphabeticlly by frequency, list is as follows"
print "-------------------------------------"
for frequency in sorted(swapped_word_dict , reverse=True):
    for words in sorted(swapped_word_dict[frequency]):
        print frequency , words
print "-------------------------------------"
