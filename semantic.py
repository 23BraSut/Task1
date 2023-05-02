import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
# You would think that monkey and banana are very close but cat and monkey are closer which was quite intresting
# Fruit vs animal and animal vs animal which now makes sense.
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# My Own
word4 = nlp("python")
word5 = nlp("java")
word6 = nlp("SQL")
# Even though they are different and use different syntax, I think due to it being programing languages
# it pickes up that they are very similar even though I thought otherwise.
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

# This shows the similarity scores between the word pairs:
# From 0 (no similarity) to 1 (perfect similarity)
# "cat" and "monkey": 0.5015
# "banana" and "monkey": 0.2433
# A cat and monkey are closer in score than a monkey and banana
# "banana" and "cat": 0.2593

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# en_core_web_sm is a small model with a limited vocabulary, designed to be lightweight and efficient, suitable for applications where speed and memory usage are important factors.
# This model contains only basic language features such as part-of-speech tags, named entities, and dependency analysis.
# en_core_web_md, on the other hand, is a larger, more complex model with a much larger vocabulary and language features.
