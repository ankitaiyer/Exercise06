
import pprint

inputfile = open("twain.txt")
filecontents = inputfile.read()

wordlist = filecontents.lower().split()
#print wordslist

word_dict = {}

# setup a dictionary of all the words, and set the value to 0
for i in wordlist:
    if i not in word_dict:
        word_dict[i] =0


# now go thru each word in the dict we made, 
# and increment every time we find it in wordlist
for i in wordlist:
    if i in word_dict:
        word_dict[i]+= 1
        #print i, word_dict[i]

pprint.pprint(word_dict)
    

