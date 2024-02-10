#import library for POS
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#import library for sentiment
from nltk.sentiment.vader import SentimentIntensityAnalyzer
SIA = SentimentIntensityAnalyzer()
from flask import Flask, render_template, request

#import library for translate
from deep_translator import GoogleTranslator
import nltk

app = Flask(__name__)

@app.route('/page')
def home():
    return render_template('Offical.html')


@app.route('/translate')
def translate():
    return render_template('translate.html')
    

    
@app.route('/sia')
def sin():
    return render_template('sann.html')
    
@app.route('/')
def ho():
    return render_template('poss.html')

@app.route('/talk',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
     
      train_text = state_union.raw("2005-GWBush.txt")
      custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
      tokenized = request.form.values()
      for i in tokenized:
                  words = nltk.word_tokenize(i)
                  tagged = nltk.pos_tag(words)
      return render_template("talking.html",result=tagged)

@app.route('/sa',methods = ['POST', 'GET'])
def map():
    if request.method == 'POST':
       SIA = SentimentIntensityAnalyzer()

       valueA =  request.form['Name']
       Values = SIA.polarity_scores(valueA)
       return render_template("neg.html",result=Values)
       

@app.route('/tra',methods = ['POST', 'GET'])
def tran():
    if request.method == 'POST':


       valueA =  request.form['Name']
       T = GoogleTranslator(source='ar', target='en').translate(valueA)
       
       return render_template("result.html",name=T)
       

          
          
@app.route('/tran',methods = ['POST', 'GET'])
def trans():
      if request.method == 'POST':


         valueE =  request.form['Name']
          
           
         M = GoogleTranslator(source='en', target='ar').translate(valueE)
     
         return render_template("result.html",name=M)

            

if __name__ == '__main__':
    app.run(debug=True, port='1080')
 
