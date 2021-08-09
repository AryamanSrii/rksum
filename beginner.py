import nltk
nltk.download("punkt")
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import pyautogui
print("enter text to summarize")
input1 = pyautogui.prompt('Enter Text To Summarize')
text = f"""{input1}"""

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)
freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue
	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]
average = int(sumValues / len(sentenceValue))
summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1 * average)):
		summary += " " + sentence
print(summary) 
res = len(text.split())
sum = len(summary.split())
quotient = sum/res
percent = quotient * 100
f = round(percent, 2)
print ("\n \nThe Number of Word in given text were " +  str(res) + " and After summarization are " + str(sum) + f" Reduced by {f}%")
pyautogui.alert(text=summary + " \n \n Number of Word in given text: " +  str(res) + " \n After summarization: " + str(sum) + f" \n Reduced by:  {f}%" , button='OK')
