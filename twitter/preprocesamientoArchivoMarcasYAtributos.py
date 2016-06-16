from nltk.corpus import stopwords
import nltk
import csv
import string

#Downloading the required corpora
#nltk.download()

def strip_punctuation(s):
    punctuation = {'/', '"'}
    for sign in punctuation:
        s = s.replace(sign, ' ')
    return s


def removeStopWords(sentence):
    sentence = sentence.lower()
    # removing punctuation symbols
    sentence = strip_punctuation(sentence)
    word_list  = nltk.word_tokenize(sentence)
    filtered_words = [word for word in word_list if word not in stopwords.words('spanish')]
    return  filtered_words


def processFile(filePath):
    result = {}
    with open(filePath, "rt") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            try:
                if(len(row)>1):
                    brand = row[0]
                    #removing head and tail spaces
                    brand= brand.strip()
                    brandAttributes = row[1]
                    brandAttributesWithoutStopWords=removeStopWords(brandAttributes)
                else:
                    brandAttributes = row[0]
                    brandAttributesWithoutStopWords = removeStopWords(brandAttributes)
                if (brand in result):
                    #adding only the non duplicate terms
                    result[brand] = result[brand]+ list(set(brandAttributesWithoutStopWords)-set(result[brand]))
                else:
                    result[brand] = brandAttributesWithoutStopWords
            except IndexError:
                print(len(row))
    print(result)

processFile('../allPreprocesado.csv')