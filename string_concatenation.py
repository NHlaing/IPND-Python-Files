sentence = "A Noun went on a walk. It can Verb really fast."
substring1 = sentence[:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

Noun_replacement = "cat"
Verb_replacement = "run"
new_sentence = substring1 + Noun_replacement + substring2 + Verb_replacement + substring3
print new_sentence
print''

sentence = "A NOUN went on a walk. It can VERB really fast."
print (sentence.find('NOUN'))
print (sentence.find('went'))
print (sentence.find('VERB'))
substring1 = sentence[0 :2]
substring2 = sentence[6:30]
substring3 = sentence[34:]
noun_replacement = "apple"
verb_replacement = "fall"
new_sentence = substring1 + noun_replacement +substring2 +verb_replacement + substring3
print (new_sentence)
