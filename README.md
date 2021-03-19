## Hi :grinning:


### Here In, this i have build a web app, which scrap the data from wikipedia :sunglasses:

## NER NLP Named Entity Recognition using NLTK and Spacy :dizzy:


 


```python
def ner(text)   
    docx = nlp(text)
     html = displacy.render(docx,style="ent")
     html = html.replace("\n\n","\n")
     result = HTML_WRAPPER.format(html)
```
