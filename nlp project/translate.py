#import library for translate
from deep_translator import GoogleTranslator
import nltk
nltk.download('vader_lexicon')

#import library for SIT
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
#SIA = SentimentIntensityAnalyzer()

#import library for POS
#import nltk
#from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer


print("ۛ ּ﷽")

answer1 = input("enter 1 to translate from Arabic to English\n or 2 to translate from English to Arabic")


if answer1 == "1":
    valueA = input("Please enter a string in Arabic:\n")
    T = GoogleTranslator(source='ar', target='en').translate(valueA)
    print(T)

elif answer1 == "2":
    valueE = input("Please enter a string in English:\n")
    M = GoogleTranslator(source='en', target='ar').translate(valueE)
    print(M)
    
else:
    print("please enter 0 or 1")
    


