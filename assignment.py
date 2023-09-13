import spacy
nlp = spacy.load("en_core_web_sm")
about_text = (
    "Gus Proto is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
)
about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)
  
# Gus 0
# Proto 4
# is 10
# a 13
# Python 15
# developer 22
# currently 32
# working 42
# for 50
# a 54
# London 56
# - 62
# based 63
# Fintech 69
# company 77
# . 84
# He 86
# is 89
# interested 92
# in 103
# learning 106
# Natural 115
# Language 123
# Processing 132
# . 142