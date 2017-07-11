from SPARQLWrapper import SPARQLWrapper, JSON
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
import functools
import time
import nltk

# pt lemmatizare
wordnet_lemmatizer = WordNetLemmatizer()
# pt queriuri
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)
# pt creare link-uri
hyperlink_format = '<a href="{link}">{text}</a>'
link_text = functools.partial(hyperlink_format.format)


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    x = tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    return x


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def eticheta_lemma(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return None


def verificaEticheta(cuvant):
    cuvant = cuvant[0:].capitalize()
    sparql.setQuery("""SELECT ?uri ?label
        WHERE {
        ?uri rdfs:label ?label .
        filter(?label=\"""" + str(cuvant) + """\"@en)
        }""")
    rezultate = sparql.query().convert()

    for i in rezultate["results"]["bindings"]:
        if "dbpedia.org" in i['uri']['value'] and "literal" in i['label']['type']:
            return True
    return False


def clasaCuvant(cuvant):
    # cuvant = cuvant.lower()
    cuvant = cuvant[0:].capitalize()
    # print "verific cuvantul:" + cuvant
    sparql.setQuery("""PREFIX dbres: <http://dbpedia.org/resource/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX dbo: <http://dbpedia.org/ontology/>

        select ?o where {dbres:""" + cuvant + """ dbo:class ?o} LIMIT 12""")
    results = sparql.query().convert()
    clasaDbpedia = ''
    for i in results["results"]["bindings"]:
        clasaDbpedia = i['o']['value']
    return clasaDbpedia


def marcaj(cuvant, clasa):
    cuvant = cuvant[0:].capitalize()
    sparql.setQuery("""SELECT ?uri ?label
        WHERE {
        ?uri rdfs:label ?label .
        ?uri dbo:class ?class .
        filter(?label=\"""" + str(cuvant) + """\"@en)
        filter(?class=<""" + clasa + """>)
        }""")
    results = sparql.query().convert()
    res = ''
    for i in results["results"]["bindings"]:
        res = i['uri']['value']
    return res


def citesteText(filename):
    with open(filename, 'r') as f:
        text = f.read()
        return text


text = citesteText("date.in")

tokens = nltk.word_tokenize(text)
tagged = nltk.pos_tag(tokens)
print(tokens)
print(tagged)
cuvinteLematizate = []


def procesare(text,numeFisier):
    cuvinteDeMarcat = []
    categoriaCuvintelor = []
    new_text = ''
    for i in range(len(tagged)):
        eticheta = eticheta_lemma(tagged[i][1])
        ok = False
        if eticheta != None and tagged[i][0] != tagged[i][1]:
            cuvant = wordnet_lemmatizer.lemmatize(tagged[i][0], eticheta)
            if cuvant.isalpha() and verificaEticheta(cuvant):
                clasa = clasaCuvant(cuvant)
                linkMarcaj = marcaj(cuvant, clasa)
                if linkMarcaj != '':
                    link = createLink(tagged[i][0],linkMarcaj)
                    ok=True
        if ok:
            new_text += link + " "
        else:
            new_text+=tagged[i][0]+" "
    with open(numeFisier + ".html", 'w') as fout:
        fout.write(new_text)

    return ([cuvinteDeMarcat, categoriaCuvintelor])

def createLink(cuvant, link):
    return link_text(link=link, text=cuvant)


start = time.time()

procesare(text,"result")

print("Timp de executie: " + str((time.time() - start)))