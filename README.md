# NER
NLP Named Entity Recognition using NLTK and Spacy


```python
def ner(text)   
    docx = nlp(text)
     html = displacy.render(docx,style="ent")
     html = html.replace("\n\n","\n")
     result = HTML_WRAPPER.format(html)
```
