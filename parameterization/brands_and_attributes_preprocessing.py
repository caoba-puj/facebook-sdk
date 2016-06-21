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

#Method used to remove any punctuation sign from a given string
def strip_punctuation(s):
    punctuation = {'/', '"'}
    for sign in punctuation:
        s = s.replace(sign, ' ')
    return s

#Method used to remove the stopwords from a given sentence
def removeStopWords(sentence):
    sentence = sentence.lower()
    # removing punctuation symbols
    sentence = strip_punctuation(sentence)
    word_list  = nltk.word_tokenize(sentence)
    filtered_words = [word for word in word_list if word not in stopwords.words('spanish')]
    return  filtered_words


#Method used to save the brand and the corresponding attributes once removed the StopWords into the database
def insertBrand(brand, brandAttributesWithoutStopWords):
    #http://blog.rastersoft.com/?p=15
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="root",
                           db="parametrization",
                           charset="utf8")
    x = conn.cursor()
    try:
        x.execute("""INSERT INTO WhoToFollow (brand,brandAttributes) VALUES (%s,%s)""", (brand, brandAttributesWithoutStopWords))
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
        insertBrand(key, str(result[key]))

logging.info("Process Started.")
processFile('../allPreprocesado.csv')
logging.info("Process Finished.")

