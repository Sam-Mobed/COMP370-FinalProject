import pandas as pd
import argparse
import json
import requests
import re
import string


def get_stopwords(url):
    response = requests.get(url)
    #print(response.content)
    bytes_string = response.content
    word_list = bytes_string.decode('utf-8').split('\n')

    # Remove empty strings from the list
    word_list = [word for word in word_list[6:] if word]

    # Print the resulting list
    return set(word_list)

'''def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-o','--output',required=True,help='Name of output json file')
    parser.add_argument('-d','--dialog',required=True,help='Name of input dialog file')

    args = parser.parse_args()

    return args.output, args.dialog'''

def replace_punctuation_with_space_regex(input_string):
    return re.sub(r'[{}]'.format(re.escape(string.punctuation)), ' ', input_string)

def count_words(input_file, stopwords):
    df = pd.read_excel(input_file)
    word_dict = {"Concerts": {}, "Culture": {}, "Movie": {}, "Personal Life": {}, "Music": {}}

    '''
    for each row, figure out what topic it is, then look at the title, description and content.
    break down the text, get rid of uninteresting words and add it to dict.
    '''

    for row in df.itertuples(index=False):
    # 'row' is a named tuple representing the row
        for word in row.Title.split():
            word = word.lower()
            word = replace_punctuation_with_space_regex(word.lower()).strip()

            if word not in stopwords: 
                    word_dict[row.Topic][word] = word_dict[row.Topic].get(word,0)+1

        for word in row.Description.split():
            word = word.lower()
            word = replace_punctuation_with_space_regex(word.lower()).strip()

            if word not in stopwords: 
                    word_dict[row.Topic][word] = word_dict[row.Topic].get(word,0)+1

        '''for word in row.Content.split():
            word = word.lower()
            word = replace_punctuation_with_space_regex(word.lower()).strip()

            if word not in stopwords: 
                    word_dict[row.Topic][word] = word_dict[row.Topic].get(word,0)+1'''

    keys_to_remove = []
    for topic in word_dict:
        for word in word_dict[topic]:
            if word_dict[topic][word]<5:
                keys_to_remove.append((topic, word))

    # Remove the keys outside the loop
    for topic, word in keys_to_remove:
        del word_dict[topic][word]
    #print(word_dict)
    #return
    with open("word_count_topics.json", "w") as fp:
        json.dump(word_dict,fp,indent=4)

if __name__ == "__main__":
    stopword_url = 'https://gist.githubusercontent.com/larsyencken/1440509/raw/53273c6c202b35ef00194d06751d8ef630e53df2/stopwords.txt'
    stopwords = get_stopwords(stopword_url)
    
    #output, dialog = get_args()
    #output = 'word_counts.json'
    #dialog = 'clean_dialog.csv'
    input_file = "FINAL_DATA.xlsx"

    count_words(input_file,stopwords)