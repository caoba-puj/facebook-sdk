#!/usr/bin/env python
#######################################################################################################################
# File used to preprocess the marcasYAtributosPreprocesado.csv file which contains all the brands and attributes. The idea is to
# obtain the relevant words (withoud stopwords) and calculate their stems.
# Finally save the results to a RDBMS like MYSQL
#######################################################################################################################
__author__ = "Wilson Alzate"
__copyright__ = "Copyright 2016, Alianza CAOBA"
__credits__ = ["Wilson Alzate"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wilson Alzate"
__email__ = "walzate@javeriana.edu.co"
__status__ = "Development"


from nltk.corpus import stopwords
import nltk
from nltk.stem import *
import csv
import string
#pip install MySQL-python
#http://stackoverflow.com/questions/26866147/mysql-python-install-fatal-error
import MySQLdb
import logging, sys
#Setting the log level
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
#Downloading the required corpora
#nltk.download()

#Method used to get the stem from a given word. This method works only for Spanish using the Snowball algorithm.
#http://www.nltk.org/api/nltk.stem.html
def stemming(word):
    stemmer = SnowballStemmer("spanish")
    result = stemmer.stem(word)
    logging.debug(result)
    return result

#Method used to iterate an array of words to get its stem and return a new arrray of stems
def stemmingListOfWords(listOfWords):
    result = []
    for word in listOfWords:
        result.append(stemming(word))
    return result

#Method used to remove any punctuation sign from a given string
def removePunctuation(s):
    punctuation = {'/', '"'}
    for sign in punctuation:
        s = s.replace(sign, ' ')
    return s

#Method used to remove the stopwords from a given sentence
def removeStopWords(sentence):
    sentence = sentence.lower()
    # removing punctuation symbols
    sentence = removePunctuation(sentence)
    word_list  = nltk.word_tokenize(sentence)
    filtered_words = [word for word in word_list if word not in stopwords.words('spanish')]
    return  filtered_words


#Method used to save the brand and the corresponding attributes once removed the StopWords into the database
def insertBrand(brand, brandAttributesWithoutStopWords, brandAttributesStems):
    #http://blog.rastersoft.com/?p=15
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="root",
                           db="parametrization",
                           charset="utf8")
    x = conn.cursor()
    try:
        x.execute("""INSERT INTO WhoToFollow (brand,brandAttributes,brandAttributesStems) VALUES (%s,%s, %s)""", (brand, brandAttributesWithoutStopWords,brandAttributesStems))
        conn.commit()
    except:
        logging.error("ERROR")
        conn.rollback()
        raise

    conn.close()

#Method used to process a CSV file with the brands and attributes. The idea is related to a brand, obtain only the
#relevant words, removing the stopwords and saving a list with the important ones.
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
                logging.error(len(row))
    logging.debug(result)

    logging.info(str(len(result)) + " items processed.")

    logging.info("Saving processed items into the database.")

    for key in result:
        logging.debug(key)
        logging.debug(result[key])
        brandAttributesStems = stemmingListOfWords(result[key])
        logging.debug(brandAttributesStems)
        insertBrand(key, str(result[key]), str(brandAttributesStems))

logging.info("Process Started.")
processFile('../marcasYAtributosPreprocesado.csv')
logging.info("Process Finished.")

