#import library for SIT
from nltk.sentiment.vader import SentimentIntensityAnalyzer
SIA = SentimentIntensityAnalyzer()



answer = input("enter 1 for English\n or 2 for Arabic")




if answer == "1":
    valueE = input("Please enter a string in English:\n")
    Values = list(SIA.polarity_scores(valueE).values(1))

    print(f'Value for Negative is    :  {Values[0]}')
    print(f'Value for Neutral  is    :  {Values[1]}')
    print(f'Value for Positive is    :  {Values[2]}')
    #print(f'Value for Compound is    :  {Values[3]}')

elif answer == "2":
    valueA = input("Please enter a string in Arabic:\n")
    Values = list(SIA.polarity_scores(valueA).values())

    print(f'Value for Negative is    :  {Values[0]}')
    print(f'Value for Neutral  is    :  {Values[1]}')
    print(f'Value for Positive is    :  {Values[2]}')
    #print(f'Value for Compound is    :  {Values[3]}')
    
else:
    print("please enter 0 or 1")


