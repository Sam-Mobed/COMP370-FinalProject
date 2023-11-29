import json
import math
import argparse

def compute_tf_idf(input_json):
    score_dict = {}
    data = None
    with open(input_json) as fp:
        data = json.load(fp)
    
    for topic in data:
        word_list = []
        #sorted_deque.insert(5)
        for word in data[topic]:
            tf = data[topic][word]
            num_topics_who_use_term = 1
            for topic2 in data:
                if topic==topic2:
                    continue
                elif word in data[topic2]:
                    num_topics_who_use_term+=1
            idf = math.log(6/num_topics_who_use_term)

            tf_idf = tf * idf
            word_list.append((word, tf_idf))
            word_list = sorted(word_list, key=lambda x: x[1])
        score_dict[topic] = [word[0] for word in word_list]

    with open('td_idf_scores.json', "w") as fp:
        json.dump(score_dict,fp,indent=4)

'''def get_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-c','--counts',required=True,help='Name of input json file')
    parser.add_argument('-n','--nwords',required=True,help='Name of output file')

    args = parser.parse_args()

    return args.counts, args.nwords'''


if __name__ == "__main__":
    #counts, nwords =  get_args()
    input_file = "word_count_topics.json"

    compute_tf_idf(input_file)