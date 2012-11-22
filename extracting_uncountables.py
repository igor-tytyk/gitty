'''
Created on Nov 22, 2012

@author: ihor
'''

import re

input_file=open('/home/ihor/enwiktionary-20121116-pages-articles.xml','r')

# creating dictionary to store the found uncountable
# nouns, creating counters and flags
uncountables={}
unc_ctr,counter=0,0
page_start,en_word=False,False

# looping through the xml file, line-by-line
for line in input_file:
    lline=line.rstrip()
	
# entering new element ('page') in the XML file
    if '<page>' in lline:
        page_start=True
        counter+=1
# saving the entry of the dictionary
    if '<title>' in lline:
        m=re.search('<title>(.*)</title>', lline)
        title=m.group(1)
# checking if the word is English (some words are of other languages
# for some reason, e.g., Hebrew)
    if re.search('==English==', lline) and page_start==True:
        en_word=True
# checking if it can be uncountable
    if re.search('{{(countable\|)?uncountable(\|\w*)?}}', lline):
# if the word is uncountable, English and within the entered element
# then we add it to the dictionary using line number as a key
        if en_word==True and page_start==True:
            uncountables[counter]=title
            unc_ctr+=1
# exiting the element and zeroing the flags
# and the title variable
    if '</page>' in lline:
        en_word, page_start=False,False
        title=''

# printing all extracted uncountable nouns
# finding out the amount of unique and non-unique uncountables     
for k,v in uncountables.iteritems():
    print k,'\t','\t', v
print 'amount of uncountables by word: ', len(uncountables)
print 'amount of uncountables by meaning: ',unc_ctr
