from xml.etree.ElementTree import *
import rdflib as rdf
import rdflib.namespace as rn
import re as re

ns={"tei":"http://www.tei-c.org/ns/1.0", "xml":"http://www.w3.org/XML/1998/namespace"}

catalogueFile = parse("C:/Users/nicco/OneDrive/Desktop/DHDK/1st Year/courses/2nd semester/KOiLaA/KOiLaA project/html5up-hyperspace/final(Tei-div-listBibl-bibl)2[1].xml")
teiNode=catalogueFile.getroot()

final_graph = rdf.Graph()

artist = rdf.Namespace("https://niccolomolinati.github.io/AroundImpressionism/artist/")
artwork = rdf.Namespace("https://niccolomolinati.github.io/AroundImpressionism/artwork/")
page = rdf.Namespace("https://niccolomolinati.github.io/AroundImpressionism/page/")
pagetype = rdf.Namespace("https://niccolomolinati.github.io/AroundImpressionism/page_type/")
handwritten = rdf.Namespace("https://niccolomolinati.github.io/AroundImpressionism/text_type/handwritten")
orgnz = rdf.Namespace("https://niccolomolinati.github.io/AroundImpressionism/organization/")

#                               --THE TRIPLES:--
#   pages rdf:label "name"
#   pages schema:text "content"
#   artist foaf:name "name"
#   work rdf:title "title"
#   work dc:creator artist
#   page dc:subject work
#   work schema:isPartOf page
#   page dc:subject artist
#   document dc:creator group
#   group rdf:label "name"
#   page rdf:type page-type
#   page-type rdf:label "type"
#   document dc:title "title"
#   document dc:spatial "place"
#   document dc:temporal "time"
#   note schema:isPartOf page
#   note rdf:type handwritten
#   note schema:text "content"
#   organization rdf:label "name"
#   document dc:provenance organization
#   document owl:sameAs identifier


# the doc is linked to the creator(1), to its title (2) and to the providers (3)
the_doc_uri = rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/document/catalogue_2nd_ex") #1
group_uri = rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/group/impressionists")
final_graph.add ((the_doc_uri, rn.DC.creator, group_uri))

title_of_doc = teiNode.findtext(".//tei:sourceDesc/tei:bibl/tei:title", default=None, namespaces=ns) #2
final_graph.add((the_doc_uri, rn.DC.title, rdf.Literal(title_of_doc)))

for org in teiNode.findall(".//tei:orgName", ns): #3
    org_id = org.text.replace(" ", "-")
    org_uri = rdf.URIRef(orgnz + org_id)
    same_doc_uri = rdf.URIRef(org.get("ref"))
    final_graph.add((org_uri, rn.RDFS.label, rdf.Literal(org.text)))
    final_graph.add((the_doc_uri, rn.DCTERMS.provenance, org_uri))
    final_graph.add((the_doc_uri, rn.OWL.sameAs, same_doc_uri))

# extracting neat and readable strings for the location and time of the exhibition
pub_place_date_node = teiNode.find(".//tei:div[@facs='page5']//tei:p[4]", namespaces=ns).itertext()
pub_date_l = list()
pub_place_l = list()
for p in pub_place_date_node:
    if "P" in p:
        pub_place_l.append(p)
    else:
        pub_date_l.append(p)
pub_place = " - ".join(pub_place_l)
pub_date = " - ".join(pub_date_l)
pub_place = pub_place.replace("\n            ", "").replace("__________", "")
pub_date = pub_date.replace("\n            ", "")
#then associating them to the file
final_graph.add((the_doc_uri, rn.DCTERMS.temporal, rdf.Literal(pub_date)))
final_graph.add((the_doc_uri, rn.DCTERMS.spatial, rdf.Literal(pub_place)))


# iterating over the div that stands for pages.
for div in teiNode.iterfind(".//tei:div[@facs]", ns):
    # naming the page
    current_page_uri = rdf.URIRef(page + div.get("facs"))
    final_graph.add((current_page_uri, rn.RDFS.label, rdf.Literal(div.get("facs"))))

    # iterating over the "empty" pages (the ones that haven't any work) and assigning to them their content text.
    if "designation-list" not in div.attrib["type"]:

    # creating a URI for each handwritten note, connecting it to its type (handwritten, to its page and to its content
        note_node = div.find(".//tei:note", ns)
        try:
            text_of_note = note_node.text
            uri_of_current_note = rdf.URIRef(handwritten + "/" + div.get("facs"))
            final_graph.add((uri_of_current_note, rn.SDO.isPartOf, current_page_uri))
            final_graph.add((uri_of_current_note, rn.RDF.type, handwritten))
            final_graph.add((uri_of_current_note, rn.SDO.text, rdf.Literal(text_of_note)))
        except:
            pass

    # giving the page a type
        type_of_page = div.get("type")
        uri_of_current_type = rdf.URIRef(pagetype + type_of_page)
        final_graph.add((current_page_uri, rn.RDF.type, uri_of_current_type))
        final_graph.add((uri_of_current_type, rn.RDFS.label, rdf.Literal(type_of_page)))
        
        content=list() #grouping content of each page and assigning it to the current page
        for child_of_div in div.itertext():
            content.append(child_of_div)

            if "Béliard-Legros-Pissaro" in child_of_div:  # naming the creator
                final_graph.add((group_uri, rn.RDFS.label, rdf.Literal(child_of_div)))
        
        text = " /n ".join(content)
        final_graph.add((current_page_uri, rn.SDO.text, rdf.Literal(text)))


    else:
        des_list = "designation-list"     #giving the page a type
        uri_of_des_list = rdf.URIRef(pagetype + des_list)
        final_graph.add((current_page_uri, rn.RDF.type, uri_of_des_list))
        final_graph.add((uri_of_des_list, rn.RDFS.label, rdf.Literal(des_list)))

    # creating a URI for each artist
        for artst in div.findall(".//tei:listBibl", ns):
            artist_name = artst.get("{http://www.w3.org/XML/1998/namespace}id")
            artist_name = artist_name.replace("_", " ")
            artist_name = re.sub("\d","", artist_name)
            artst_id = artist_name.replace(" ", "-")
            current_artist_uri = rdf.URIRef(artist + artst_id)
            final_graph.add((current_artist_uri, rn.FOAF.name, rdf.Literal(artist_name)))
            final_graph.add((current_page_uri, rn.DC.subject, current_artist_uri))
            final_graph.add((current_artist_uri, rn.SDO.isPartOf, group_uri))
            
            #current_artist_uri = rdf.URIRef(artist + artst_id)
            #print(artist_name,current_artist_uri)
            # each artist is connected to its name, to their pages and to the group of creators
            #final_graph.add((current_artist_uri, rn.FOAF.name, rdf.Literal(artist_name)))
            #final_graph.add((current_page_uri, rn.DC.subject, current_artist_uri))
            #final_graph.add((current_artist_uri, rn.SDO.isPartOf, group_uri))

            
    # iterating into every list to get a URI of each work
            for work in artst.findall("./tei:bibl", ns):
                title_of_current_work = work.findtext("./tei:title", namespaces=ns)
                work_name_for_uri = title_of_current_work.replace("  ","").replace(" ","-").replace("'","-")
                work_name_for_uri= re.sub("\n","-", work_name_for_uri)
                current_work_uri = rdf.URIRef(artwork + work_name_for_uri)
                final_graph.add((current_work_uri, rn.DC.title, rdf.Literal(title_of_current_work)))
                final_graph.add((current_work_uri, rn.DC.creator, current_artist_uri))
                final_graph.add((current_page_uri, rn.DC.subject, current_work_uri))
                final_graph.add((current_work_uri, rn.SDO.isPartOf, current_page_uri))

final_graph.serialize(destination="RDFfromXMLfinal.rdf")
