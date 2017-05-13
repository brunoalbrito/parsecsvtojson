import csv

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF


g = Graph()

texto = []

with open("example.csv","r") as f:
    spamreader = csv.reader(f, delimiter=',', quotechar='"')
    spamreader.next()
    for row in spamreader:
        texto.append(row)
        
    dicionario = {}
    
    for j in range(len(texto)):
        dicionario[texto[j][1]] = BNode() 
        
    
    for i in range(len(texto)):
        g.add( (dicionario[str(texto[i][1])], RDF.type, FOAF.Person) )
        g.add( (dicionario[str(texto[i][1])], FOAF.nick, Literal(str(texto[i][1]), lang="foo")) )
        g.add( (dicionario[str(texto[i][1])], FOAF.name, Literal(texto[i][2])) )
        g.add( (dicionario[str(texto[i][1])], FOAF.mbox, URIRef("mailto:"+str(texto[i][3]))) )
        for p in dicionario.keys():
            if p == texto[i][4]: 
                g.add( (dicionario[str(texto[i][1])], FOAF.knows, dicionario[p]))

g.serialize(destination='sucesso.json', format='json-ld')
file = open("sucesso.json", "w")
file.write(g.serialize(format='json-ld'))
    
    
"""g.serialize(destination='bruno.rdf', format='application/rdf+xml')
file = open("bruno.rdf", "w")
file.write(g.serialize(format='application/rdf+xml'))    """