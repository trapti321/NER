## Hi :grinning:


### Here In this i have build a web app, which scrap the data from wikipedia :sunglasses:

## NER NLP Named Entity Recognition using NLTK and Spacy :dizzy:
 
#### Steps 

To build the API, we will need to create two files:
 1. index.html to handle the template of the API.
 2. app.py to handle the requests and return the output file. 
 
 ## app.py
  It contains the main code that will be executed by the Python interpreter to run the Flask web application, it includes the spaCy code for recognizing named entities.
  We ran our app as a single module; thus we initialized a new Flask instance with the argument __name__ to let Flask know that it can find the HTML template folder (templates)   in the same directory where it is located.
 We use the route decorator (@app.route('/')) to specify the URL that should trigger the execution of the index function.
 Our index function simply rendered the index.html HTML file, which is located in the templates folder.
 Inside the process function, we apply nlp to the raw text user will enter, and extract pre-determined named entities (Organization, Person, Geopolitical & Money) from the raw    text.
We use the POST method to transport the form data to the server in the message body. Finally, by setting the debug=True argument inside the app.run method, we further activated Flask's debugger.
We use the run function to only run the application on the server when this script is directly executed by the Python interpreter, which we ensured using the if statement with __name__ == '__main__'.

## Try our API

Start the Command Prompt.
Navigate to our Named-Entity-Extractor folder.

### Open your Web browser, copy-paste ``“http://127.0.0.1:5000/”`` into the address bar, and we will see this form.

Visit: https://github.com/trapti321/NER/blob/ner/Doc3.png


```python
def ner(text)   
    docx = nlp(text)
     html = displacy.render(docx,style="ent")
     html = html.replace("\n\n","\n")
     result = HTML_WRAPPER.format(html)
```
## References
### Visit: https://stackabuse.com/python-for-nlp-parts-of-speech-tagging-and-named-entity-recognition/ 
### Visit: https://pypi.org/project/wikipedia-ner/


### Also you can do with Jupyter Notebook
## Inbuild library ***Wikipedia***

```python
import wikipedia
from spacy import displacy
sp = spacy.load('en_core_web_sm')

strr = input('Enter your search:')
print(wikipedia.search(strr)) #sentence=5))
complete_content = wikipedia.page(strr)
print(complete_content.content)

sen = sp(complete_content.content)
displacy.render(sen, style='ent', jupyter=True)

```
