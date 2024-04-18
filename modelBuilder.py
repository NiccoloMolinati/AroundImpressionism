import pandas as pd
import rdflib as rdf
from rdflib.namespace import FOAF, DC, RDF, RDFS, OWL, DCTERMS, SDO,SKOS

the_model = rdf.Graph()

dbo = rdf.Namespace("http://dbpedia.org/ontology/")
dbnt = rdf.Namespace("https://d-nb.info/standards/elementset/dnb#")
bf = rdf.Namespace("http://id.loc.gov/ontologies/bibframe/")
rico = rdf.Namespace("https://www.ica.org/standards/RiC/ontology/")
fabio = rdf.Namespace("http://purl.org/spar/fabio")
crm = rdf.Namespace("http://www.cidoc-crm.org/cidoc-crm/")
media = rdf.Namespace("http://purl.org/media")
bibo = rdf.Namespace("http://purl.org/ontology/bibo/")
cdesc = rdf.Namespace("https://w3id.org/arco/ontology/context-description/")
madsrdf = rdf.Namespace("http://www.loc.gov/mads/rdf/v1#")
bio = rdf.Namespace("http://purl.org/vocab/bio/0.1/")
cevent = rdf.Namespace("https://w3id.org/arco/ontology/cultural-event")
tl = rdf.Namespace("http://purl.org/NET/c4dm/timeline.owl#/")
the_model.bind("rdf", RDF)
the_model.bind("foaf",FOAF)
the_model.bind("dcterms",DCTERMS)
the_model.bind("owl", OWL)
the_model.bind("schema",SDO)
the_model.bind("dbo", dbo)
the_model.bind("dbnt",dbnt)
the_model.bind("bf",bf)
the_model.bind("rico",rico)
the_model.bind("fabio",fabio)
the_model.bind("crm",crm)
the_model.bind("media",media)
the_model.bind("bibo",bibo)
the_model.bind("cdesc",cdesc)
the_model.bind("madsrdf",madsrdf)
the_model.bind("bio",bio)
the_model.bind("cevent",cevent)
the_model.bind("tl",tl)


main_path = "C:/Users/nicco/OneDrive/Desktop/DHDK/1st Year/courses/2nd semester/KOiLaA/KOiLaA project/html5up-hyperspace/"
files = {"record":"Carneige audio file.csv", "cat":"Catalogue.csv", "podcast":"Claude Monet.csv", "sketch":"Hat pinning.csv",
         "imp book":"Impressionism book.csv", "imp film":"Impressionism film.csv", "tomb":"Photo of the Tomb.csv",
         "portrait":"Portrait of Monet.csv", "rose":"Rose Edgar.csv", "sculpture":"Sculpture .csv"}

items_uri= {"Photo of the tomb":"http://catalogue.bnf.fr/ark:/12148/cb40499435z","Portrait of Monet":"http://www.deutschefotothek.de/documents/obj/70222045",
            "Catalogue of the second exhibition":"http://catalogue.bnf.fr/ark:/12148/btv1b8618484c","the hat pinning (painting)":"https://sammlungenonline.albertina.at/?query=search=/record/objectnumbersearch=[DG1912/210]&showtype=record",
            "the sculpture":"http://id.bildindex.de/thing/0001567049", 'Rose "Edgar Degas"':"https://niccolomolinati.github.io/AroundImpressionism/Object/DegasRose",
            "Impressionism : reflections and perceptions":"https://niccolomolinati.github.io/AroundImpressionism/Object/ImpressionismBook", 
            "Impressionism film":"https://niccolomolinati.github.io/AroundImpressionism/Object/ImpressionismFilm",
            'Claude Monet and the "Birth" of Impressionism':"https://niccolomolinati.github.io/AroundImpressionism/Object/ImpressionismPodcast", 
            "The Carnegie Hall Library Of Classical Music":"https://niccolomolinati.github.io/AroundImpressionism/Object/ImpressionismMusic"}

prop_needing_uri = ("rdf:type", "dcterms:subject", "crm:P43_has_dimension", "fabio:has_format", "schema:provider", 
                    "dcterms:creator", "dcterms:publisher", "dcterms:contributor", "rdfs:label", "cdesc:hasGenus")

objects = {"Podcast":"https://schema.org/AudioObject", "Audio":"https://schema.org/MusicRecording", "Book":"https://schema.org/Book",
            "photograph":"https://schema.org/Photograph", "Color lithograph":"https://schema.org/Photograph",
            "Sculpture":"https://schema.org/Sculpture", "Plant":"https://w3id.org/arco/ontology/context-description/BiologicalTaxon", "Doug Bailey Films":"http://viaf.org/viaf/263723254",
            "Internet Archive":"http://viaf.org/viaf/5838148574318224430007", "Claude Debussy":"http://viaf.org/viaf/6219636",
            "Frederick Delius":"http://viaf.org/viaf/51874944", "Ralph Vaughan Williams":"http://viaf.org/viaf/89801735", 
            "Maurice Ravel":"http://viaf.org/viaf/2657495", "Manuel De Falla":"http://viaf.org/viaf/42025164",
            "George Braziller":"http://viaf.org/viaf/159803619", "Meyer Schapiro":"http://viaf.org/viaf/5009565", 
            "Dr. Sarah C. Schaefer":"http://viaf.org/viaf/310631717", "Dr. Tina Rivers Ryan":"http://viaf.org/viaf/315996621",
            'State of Arts: Claude Monet and the "Birth" of Impressionism':"http://viaf.org/viaf/184369877", "Apple iTunes":"http://viaf.org/viaf/186435690",
            "Aristide Maillol":"http://viaf.org/viaf/14228", "Guy Delbard":"https://niccolomolinati.github.io/AroundImpressionism/Person/Delbard", "University of Trieste":"http://viaf.org/viaf/145362602", 
            "Italy":"http://viaf.org/viaf/152361066", "France":"http://viaf.org/viaf/264091107", "BNF":"http://viaf.org/viaf/137156173", 
            "Claude Monet":"http://viaf.org/viaf/24605513","Edgar Degas":"https://niccolomolinati.github.io/AroundImpressionism/Person/Degas", 
            "Pierre-Auguste Renoir":"http://viaf.org/viaf/29643005",
            "Agencie de presse Maurisse":"http://viaf.org/viaf/143525780", "Germany":"http://viaf.org/viaf/189116956",
            "height":"http://www.cidoc-crm.org/cidoc-crm/E54_Dimension", "width":"http://www.cidoc-crm.org/cidoc-crm/E54_Dimension",
            "Impressionism":"https://dbpedia.org/page/Category:Impressionism", " Classical":"https://dbpedia.org/ontology/ClassicalMusicComposition",
            "Bibliography":"https://dbpedia.org/page/Category:Bibliography", "Visual Arts":"https://dbpedia.org/page/Category:Visual_arts_media",
            "Artists of the 2nd exhibition":"https://dbpedia.org/page/Category:French_Impressionist_painters","Woman with a parasol":"https://dbpedia.org/page/Woman_with_a_Parasol_%E2%80%93_Madame_Monet_and_Her_Son",
            "portrait":"https://dbpedia.org/page/Category:Portraits", "Deutsches Fotothek":"http://viaf.org/viaf/128500931",
            "Rosa Cultivar":"https://dbpedia.org/page/Cultivar", "Patrician Films":"https://niccolomolinati.github.io/AroundImpressionism/Event/PatriciainFilms",
            "Hollywood/ Calif. : Bailey Films":"https://niccolomolinati.github.io/AroundImpressionism/Event/BaileyFilms",
            "Second exhibition":"https://niccolomolinati.github.io/AroundImpressionism/Event/SecondExhibition",
            "Giverny Church Cemetery":"https://niccolomolinati.github.io/AroundImpressionism/Object/GivernyChurch",
            "Tomb of Monet":"https://niccolomolinati.github.io/AroundImpressionism/Object/MonetTomb",
            "Archive of digital images of vascular plants from projects Dryades":"https://niccolomolinati.github.io/AroundImpressionism/Object/PlantsArchive",
            "Death of Monet":"https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfMonet",
            "Text":"http://purl.org/dc/dcmitype/Text", "print book":"http://purl.org/spar/fabio/CriticalEdition",
            "Film":"https://schema.org/Movie", "close up":"", "Rosa":"https://dbpedia.org/page/Rose", "pink":"https://dbpedia.org/page/Pink",
            "yellow":"https://dbpedia.org/page/Yellow"
            }

for csv_file in files:

    file_df = pd.read_csv(main_path+files[csv_file]) #reading the file
    item_uri = rdf.URIRef(items_uri[file_df.loc[0].iloc[0]])              #<-- need a URI
    the_model.add((item_uri, DCTERMS.title, rdf.Literal(file_df.loc[0].iloc[0]))) # dc:title of the item

    for idx, triple in file_df.iterrows(): #iter over every triple
        pred_uri_list = triple["Predicate"].split(":")
        pred_ns = pred_uri_list[0]
        pred_prop = pred_uri_list[1]

        pred_uri = rdf.URIRef(pred_ns+pred_prop) #then reunite it to create the URI of the predicate, but for some reason this doesn't work properly

        if triple["Predicate"] in prop_needing_uri:    #if the object needs a URI:
            obj = triple["Object"]
            if obj =="Various" or obj=="UNKNOWN":
                the_model.add((item_uri, pred_uri, rdf.Literal(obj)))
            elif triple["Predicate"] == "crm:P43_has_dimension":
                    obj_list = triple["Object"].split(" ")
                    obj_uri = rdf.URIRef(item_uri+obj_list[0])     
                    the_model.add((item_uri, pred_uri, obj_uri))
                    the_model.add((obj_uri, RDFS.label, rdf.Literal(triple["Object"])))
            else:
                obj_uri = rdf.URIRef(objects[obj])        #call the URI assigned to it
                if obj not in ["Guy Delbard", "Claude Monet", "Claude Debussy","Dr. Sarah C. Schaefer", "Dr. Tina Rivers Ryan",
                               "Edgar Degas","Frederick Delius","George Braziller","Manuel De Falla","Maurice Ravel","Meyer Schapiro",
                               "Pierre-Auguste Renoir","Ralph Vaughan Williams"]:
                    the_model.add((obj_uri, RDFS.label, rdf.Literal(obj)))
                the_model.add((item_uri, pred_uri, obj_uri))     #add it
                if triple["Predicate"] == "dcterms:creator":
                    the_model.add((obj_uri, rdf.URIRef(rico["isAuthorOf"]), item_uri))

        else:
            the_model.add((item_uri, pred_uri, rdf.Literal(triple["Object"]))) #otherwise, add the literal'''

# to do:
#person has name
the_model.add((rdf.URIRef(objects["Guy Delbard"]), FOAF.firstName, rdf.Literal("Guy")))
the_model.add((rdf.URIRef(objects["Claude Debussy"]), FOAF.firstName,  rdf.Literal("Claude")))
the_model.add((rdf.URIRef(objects["Claude Monet"]), FOAF.firstName,  rdf.Literal("Claude")))
the_model.add((rdf.URIRef(objects["Dr. Sarah C. Schaefer"]), FOAF.firstName,  rdf.Literal("Sarah C.")))
the_model.add((rdf.URIRef(objects["Dr. Tina Rivers Ryan"]), FOAF.firstName,  rdf.Literal("Tina")))
the_model.add((rdf.URIRef(objects["Edgar Degas"]), FOAF.firstName,  rdf.Literal("Edgar")))
the_model.add((rdf.URIRef(objects["Frederick Delius"]), FOAF.firstName,  rdf.Literal("Frederick")))
the_model.add((rdf.URIRef(objects["George Braziller"]), FOAF.firstName,  rdf.Literal("George")))
the_model.add((rdf.URIRef(objects["Manuel De Falla"]), FOAF.firstName,  rdf.Literal("Manuel")))
the_model.add((rdf.URIRef(objects["Maurice Ravel"]), FOAF.firstName,  rdf.Literal("Maurice")))
the_model.add((rdf.URIRef(objects["Meyer Schapiro"]), FOAF.firstName,  rdf.Literal("Meyer")))
the_model.add((rdf.URIRef(objects["Pierre-Auguste Renoir"]), FOAF.firstName,  rdf.Literal("Pierre-Auguste")))
the_model.add((rdf.URIRef(objects["Ralph Vaughan Williams"]), FOAF.firstName,  rdf.Literal("Ralph")))
#person has surname
the_model.add((rdf.URIRef(objects["Guy Delbard"]), FOAF.lastName, rdf.Literal("Delbard")))
the_model.add((rdf.URIRef(objects["Claude Debussy"]), FOAF.lastName,  rdf.Literal("Debussy")))
the_model.add((rdf.URIRef(objects["Claude Monet"]), FOAF.lastName,  rdf.Literal("Monet")))
the_model.add((rdf.URIRef(objects["Dr. Sarah C. Schaefer"]), FOAF.lastName,  rdf.Literal("Schafer")))
the_model.add((rdf.URIRef(objects["Dr. Tina Rivers Ryan"]), FOAF.lastName,  rdf.Literal("Rivers Ryan")))
the_model.add((rdf.URIRef(objects["Edgar Degas"]), FOAF.lastName,  rdf.Literal("Degas")))
the_model.add((rdf.URIRef(objects["Frederick Delius"]), FOAF.lastName,  rdf.Literal("Delius")))
the_model.add((rdf.URIRef(objects["George Braziller"]), FOAF.lastName,  rdf.Literal("Braziller")))
the_model.add((rdf.URIRef(objects["Manuel De Falla"]), FOAF.lastName,  rdf.Literal("De Falla")))
the_model.add((rdf.URIRef(objects["Maurice Ravel"]), FOAF.lastName,  rdf.Literal("Ravel")))
the_model.add((rdf.URIRef(objects["Meyer Schapiro"]), FOAF.lastName,  rdf.Literal("Schapiro")))
the_model.add((rdf.URIRef(objects["Pierre-Auguste Renoir"]), FOAF.lastName,  rdf.Literal("Renoir")))
the_model.add((rdf.URIRef(objects["Ralph Vaughan Williams"]), FOAF.lastName,  rdf.Literal("Vaughan Williams")))
#person has gender
the_model.add((rdf.URIRef(objects["Guy Delbard"]), FOAF.gender, rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Claude Debussy"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Claude Monet"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Dr. Sarah C. Schaefer"]), FOAF.gender,  rdf.Literal("Female")))
the_model.add((rdf.URIRef(objects["Dr. Tina Rivers Ryan"]), FOAF.gender,  rdf.Literal("Female")))
the_model.add((rdf.URIRef(objects["Edgar Degas"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Frederick Delius"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["George Braziller"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Manuel De Falla"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Maurice Ravel"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Meyer Schapiro"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Pierre-Auguste Renoir"]), FOAF.gender,  rdf.Literal("Male")))
the_model.add((rdf.URIRef(objects["Ralph Vaughan Williams"]), FOAF.gender,  rdf.Literal("Male")))
#person has occupation
the_model.add((rdf.URIRef(objects["Claude Monet"]), rdf.URIRef(madsrdf["occupation"]), rdf.URIRef("https://dbpedia.org/ontology/Artist")))
the_model.add((rdf.URIRef(objects["Edgar Degas"]), rdf.URIRef(madsrdf["occupation"]), rdf.URIRef("https://dbpedia.org/ontology/Artist")))
the_model.add((rdf.URIRef(objects["Pierre-Auguste Renoir"]), rdf.URIRef(madsrdf["occupation"]), rdf.URIRef("https://dbpedia.org/ontology/Artist")))
the_model.add((rdf.URIRef("https://dbpedia.org/ontology/Artist"), RDFS.label, rdf.Literal("Artist")))
#artist isPrimary topic of impressionism
the_model.add((rdf.URIRef("https://dbpedia.org/ontology/Artist"), FOAF.isPrimaryTopicOf, rdf.URIRef(objects["Impressionism"])))
#artist has death
the_model.add((rdf.URIRef(objects["Claude Monet"]), rdf.URIRef(bio["agent"]), rdf.URIRef(objects["Death of Monet"])))
the_model.add((rdf.URIRef(objects["Edgar Degas"]), rdf.URIRef(bio["agent"]), rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfDegas")))
the_model.add((rdf.URIRef(objects["Pierre-Auguste Renoir"]), rdf.URIRef(bio["agent"]), rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfRenoir")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfDegas"), RDFS.label,rdf.Literal("Death of Degas")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfRenoir"), RDFS.label, rdf.Literal("Death of Renoir")))
#artist has birth
the_model.add((rdf.URIRef(objects["Claude Monet"]), rdf.URIRef(bio["agent"]), rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfMonet")))
the_model.add((rdf.URIRef(objects["Edgar Degas"]), rdf.URIRef(bio["agent"]), rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfDegas")))
the_model.add((rdf.URIRef(objects["Pierre-Auguste Renoir"]), rdf.URIRef(bio["agent"]), rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfRenoir")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfMonet"), RDFS.label,rdf.Literal("Birth of Monet")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfDegas"), RDFS.label,rdf.Literal("Birth of Degas")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfRenoir"), RDFS.label,rdf.Literal("Birth of Renoir")))

#death has place
the_model.add((rdf.URIRef(objects["Death of Monet"]), rdf.URIRef(bio["date"]), rdf.Literal("december 5th, 1926")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfDegas"),rdf.URIRef(bio["date"]),rdf.Literal("september 27th 1917")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfRenoir"),rdf.URIRef(bio["date"]),rdf.Literal("december 3rd 1919")))
#death has time
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfMonet"), rdf.URIRef(bio["place"]), rdf.Literal("Giverny, France")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfDegas"),rdf.URIRef(bio["place"]),rdf.Literal("Paris, France")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/DeathOfRenoir"),rdf.URIRef(bio["place"]),rdf.Literal("Cagnes-Sur-Mere, France")))
#birth has place
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfMonet"), rdf.URIRef(bio["date"]), rdf.Literal("november 14th, 1840")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfDegas"),rdf.URIRef(bio["date"]),rdf.Literal("july 19th 1834")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfRenoir"),rdf.URIRef(bio["date"]),rdf.Literal("february 25th 1841")))
#birth has time
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfMonet"), rdf.URIRef(bio["place"]), rdf.Literal("Paris, France")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfDegas"),rdf.URIRef(bio["place"]),rdf.Literal("Paris, France")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/BirthOfRenoir"),rdf.URIRef(bio["place"]),rdf.Literal("Limoges, France")))

#2nd exhibition creator artists
the_model.add((rdf.URIRef(objects["Second exhibition"]), DCTERMS.creator, rdf.URIRef(objects["Artists of the 2nd exhibition"])))
#2ns ex. is in place
the_model.add((rdf.URIRef(objects["Second exhibition"]), rdf.URIRef(cevent["eventTimeLocation"]), rdf.Literal("April 1876, Durand-Ruel gallery, 11 rue Le Peletier, Paris")))
#2nd ex. comes after 1st ex.
the_model.add((rdf.URIRef(objects["Second exhibition"]), rdf.URIRef(cevent["hasPreviousSituation"]), rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/FirstExhibition")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/FirstExhibition"), RDFS.label, rdf.Literal("First exhibition")))
#1st ex. is in place/time
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/FirstExhibition"), rdf.URIRef(cevent["eventTimeLocation"]), rdf.Literal("april 15th-may 15th 1874, 35 Boulevard des Capucines, Paris")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/FirstExhibition"), rdf.URIRef(tl["atDuration"]), rdf.Literal("april 15th-may15th 1874")))
#1st ex has creator
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Event/FirstExhibition"), DCTERMS.creator, rdf.URIRef(objects["Artists of the 2nd exhibition"])))
#tomb of monet is in place
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Object/MonetTomb"), rdf.URIRef(rico["location"]), rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Object/GivernyChurch")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Object/GivernyChurch"), RDFS.label, rdf.Literal("Giverny Church")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Object/GivernyChurch"), rdf.URIRef(rico["location"]),rdf.URIRef("http://viaf.org/viaf/140745829")))
the_model.add((rdf.URIRef("http://viaf.org/viaf/140745829"), RDFS.label, rdf.Literal("Giverny")))
#tomb of monet created in
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Object/MonetTomb"), rdf.URIRef(rico["creationDate"]), rdf.Literal("december 10th, 1926")))
the_model.add((rdf.URIRef("https://niccolomolinati.github.io/AroundImpressionism/Object/MonetTomb"), RDFS.label, rdf.Literal("Tomb of Monet")))
#impressionism creator artists
the_model.add((rdf.URIRef(objects["Impressionism"]), DCTERMS.creator, rdf.URIRef(objects["Artists of the 2nd exhibition"])))
#artists is artist
the_model.add((rdf.URIRef(objects["Artists of the 2nd exhibition"]), RDF.type, rdf.URIRef("https://dbpedia.org/ontology/Artist")))
#the woman with a parasol is created in 1875
the_model.add((rdf.URIRef(objects["Woman with a parasol"]), rdf.URIRef(rico["creadionDate"]), rdf.Literal("1875")))
#twwap creator monet
the_model.add((rdf.URIRef(objects["Woman with a parasol"]), DCTERMS.creator, rdf.URIRef(objects["Claude Monet"])))
#twwap type painting
the_model.add((rdf.URIRef(objects["Woman with a parasol"]), RDF.type, rdf.URIRef("https://schema.org/Painting")))
the_model.add((rdf.URIRef("https://schema.org/Painting"), RDFS.label, rdf.Literal("painting")))
#rosa has type genus
the_model.add((rdf.URIRef(objects["Rosa"]), RDF.type, rdf.URIRef("https://w3id.org/arco/ontology/context-description/Genus")))
the_model.add((rdf.URIRef("https://w3id.org/arco/ontology/context-description/Genus"), RDFS.label, rdf.Literal("Genus")))

#owl:sameAs:
the_model.add((rdf.URIRef(items_uri['Rose "Edgar Degas"']), OWL.sameAs, rdf.URIRef("https://www.wikidata.org/wiki/Q28869614")))
the_model.add((rdf.URIRef("http://viaf.org/viaf/140745829"), OWL.sameAs, rdf.URIRef("http://vocab.getty.edu/page/tgn/7009209")))
the_model.add((rdf.URIRef(objects["Edgar Degas"]), OWL.sameAs, rdf.URIRef("http://viaf.org/viaf/41863744")))

#5 associations:
the_model.add((rdf.URIRef(objects["Text"]), SKOS.narrower, rdf.URIRef(objects["Book"])))
the_model.add((rdf.URIRef("https://schema.org/Painting"), SKOS.broader, rdf.URIRef("https://schema.org/CreativeWork")))
the_model.add((rdf.URIRef(objects["Audio"]), SKOS.related, rdf.URIRef(objects["Podcast"])))
the_model.add((rdf.URIRef("https://schema.org/CreativeWork"), SKOS.narrowerTransitive, rdf.URIRef(objects["Audio"])))
the_model.add((rdf.URIRef("https://schema.org/CreativeWork"), SKOS.narrowerTransitive, rdf.URIRef(objects["Text"])))

the_model.serialize("final_RDF_model5.rdf")