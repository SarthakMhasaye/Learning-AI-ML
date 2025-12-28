#  NER is a language processing techniqueused to identify and classifynamed entitiy in text into predefined category suxh as 
# Person name,organization name,location,date and time

# HOw NER WORKS  !!!
# Step 1: TokenizationO
# step 2: POS Identifaction : identify part of speech
# step 3: Entity detection


# NLTK LIbrary - NER
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag,ne_chunk
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# Sample text
sentence = "Barak Obama was born in huwaii and was the 44th president of united states"

# Tokenize the sentence
tokens = word_tokenize(sentence)
print(f"\n Token's : ",tokens)

# Pos Tagging
pos_tags = pos_tag(tokens)
print("\n Pos tags:",pos_tags)

# Performed NER
try:
    named_entities = ne_chunk(pos_tags)
    print("Named Entites:")
    named_entities.pprint()
except Exception as e:
    print("\n Error during named entity recognizer",str(e))  
