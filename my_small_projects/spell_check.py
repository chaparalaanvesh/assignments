""" create functions and build a spell checker."""



def clean_text(text_string, special_characters):
    cleaned_string = text_string
    for string in special_characters:
        cleaned_string = cleaned_string.replace(string, "")
    cleaned_string = cleaned_string.lower()
    return(cleaned_string)

def tokenize(text_string, special_characters, clean=False):
    cleaned_text = text_string
    if clean:
        cleaned_text = clean_text(text_string, special_characters)
    tokens = cleaned_text.split(" ")
    return(tokens)
final_misspelled_words = []
def spell_check(vocabulary_file,text_file,special_characters = [",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary_file_read = open(vocabulary_file).read()
    text = open(text_file).read()
    tokenized_vocabulary = tokenize(vocabulary_file_read,special_characters)
    tokenized_text = tokenize(text,special_characters,True)
    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return(misspelled_words)



final_misspelled_words= spell_check(vocabulary_file='dictionary.txt',text_file='story.txt')
print(final_misspelled_words)
