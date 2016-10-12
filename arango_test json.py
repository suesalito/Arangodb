from rdflib import Graph, plugin
from rdflib.serializer import Serializer
testrdf = '''
@prefix dc: <http://purl.org/dc/terms/> .
<http://example.org/about>
dc:title "Someone's Homepage"@en .
'''
g = Graph().parse(data=testrdf, format='n3')
# print(g.serialize(format='json-ld', indent=4))

print(g.serialize(format='json-ld', indent=4).decode('utf-8'))

#
# <http://www.drugbank.ca/system/downloads/current/drugbank.xml.zip>
# <http://www.w3.org/2000/01/rdf-schema#label>
# #  "DrugBank (drugbank.xml.zip)"
# # <http://bio2rdf.org/drugbank_resource:bio2rdf.dataset.drugbank.R3> .
