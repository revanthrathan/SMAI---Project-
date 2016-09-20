import nltk
import codecs

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_list = stopwords.words('english')
stop_set = set(stop_list)

writeFile = codecs.open("output.txt", "w", encoding='utf-8')

with codecs.open("input.txt", "r", encoding='utf-8') as f:
	line = f.read()
    	element = nltk.word_tokenize(line)
    	element = [w for w in element if w not in stop_set]
    	for i in element:
        	writeFile.write(i)
        	if len(i) != 1:
        		writeFile.write(' ')






