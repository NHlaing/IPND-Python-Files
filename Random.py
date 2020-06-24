from random import randint
def random_verb():
    random_num = randint(0,1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint (0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == 'Noun':
        return random_noun()
    if word == 'Verb':
        return random_verb()
    else:
        return word[0]


def process_madlib(madlib):
    processed = ""
    index = 0
    box_length = 4
    while index < len(madlib):
        frame = madlib [index: index + box_length]
        to_add = word_transformer(frame)
        processed += to_add
        if len(to_add) == 1:
            index += 1
        else:
            index += 4
    return processed

test_string_1 = "This is a good Noun to use when you Verb your food"
test_string_2 = "I'm going to Verb to the store and pick up a Noun or two."
print (process_madlib(test_string_1))
print (process_madlib(test_string_2))
