# Todo - error handling for reading file
import itertools
import matplotlib.pyplot as plt
import nltk
import re
import sys

""" Uncomment the line below to download the nltk corpora,
    if not already downloaded
"""
#nltk.download()
from nltk.corpus import stopwords

''' returns the contents (as a string) of the input file '''
def read_input_file():
    input_file = sys.argv[1]  # get filename from command line
    f = open(input_file, 'r')
    contents = f.read()  # save contents of file
    f.close()
    return contents
    #return "Error reading input file"

''' given a string, returns all the tokens (words)
    as elements in a list. Gets rid of punctuation, too.
'''
def tokenize(contents):
    # remove punctuation
    contents = re.sub('[(){}<>,?!.:;]', '', contents)
    # use whitespace as deliminator for tokenization 
    contents = contents.split()
    # lowercase all tokens for easy stopword removal later
    contents = [word.lower() for word in contents]
    return contents
    
''' removes stopwords (commonly used words, e.g. 'the')
    from the token list
'''
def remove_stopwords(tokens, stopword_list):
    for stopword in stopword_list:
        tokens = [tkn for tkn in tokens if tkn != stopword]
    return tokens

''' returns a dict of { token : # of appearances } '''
def organize_tokens(tokens):
    token_dict = {tkn : tokens.count(tkn) for tkn in tokens }
    return dict(sorted(token_dict.items(), key = lambda k: k[1], reverse=True))

''' creates a piechart of the top 10 words '''
def create_piechart(tokens):
    if len(tokens) > 10:
        tokens = dict(itertools.islice(tokens.items(), 10))
    words = [x for x, y in tokens.items()]
    count  = [y for x, y in tokens.items()]

    plt.pie(count, labels=words, autopct=lambda p: '{:.0f}'.format(p * sum(count) / 100))
    plt.axis('equal')
    plt.title('Ten Most Frequently Used Words in the Document')
    plt.savefig('piechart.png')
    plt.show()
    

def print_stats(total_word_count, token_dict):
    print("")
    print("There are", total_word_count, "words total in the document.")
    print("")
    print(token_dict)

def main():
    stopword_list = stopwords.words("english")
    file_contents = read_input_file()
    tokens = tokenize(file_contents)
    total_word_count = len(tokens)  # to keep track of word count
    tokens = remove_stopwords(tokens, stopword_list)
    token_dict = organize_tokens(tokens)
    create_piechart(token_dict)
    print_stats(total_word_count, token_dict)

main()