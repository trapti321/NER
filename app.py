from flask import Flask,url_for,render_template,request
from flaskext.markdown import Markdown
import requests
import nltk
import urllib
import bs4 as bs
import re 


# NLP Pkgs
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
import json

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

# Init
app = Flask(__name__)
Markdown(app)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/extract',methods=["GET","POST"])
def extract():
	if request.method == 'POST':

            searchString = request.form['rawtext'].replace(" ","_") 
            url = "https://en.wikipedia.org/wiki/" + searchString
            source = urllib.request.urlopen(url)
            soup = bs.BeautifulSoup(source,features="html.parser")

            text = ""
            for para in soup.find_all('p',limit=5):
                text = text+para.text

                text = re.sub(r'\n',' ',text)
                text = re.sub(r'\[[0-9]*\]',' ',text)
                text = re.sub(r'\ \' ',' ',text)
                text = text.replace("\'","") 

                # preprocess
                text = text.split('.')
                text =text[0:15]
                text = str(text)
                text = text.replace("', '",".") 
                text =text.replace("['","") 
                text = text.replace("']",".")

            docx = nlp(text)
            html = displacy.render(docx,style="ent")
            html = html.replace("\n\n","\n")
            result = HTML_WRAPPER.format(html)

	return render_template('result.html',result=result)




if __name__ == '__main__':
	app.run(debug=True)
