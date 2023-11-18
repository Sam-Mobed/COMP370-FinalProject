import argparse
import json
import pandas as pd

def parse_text(text):
    #parses text to make sure that title/description of article mentions Taylor Swift, Travis, Eras,...
    pass

def collect_posts(outfile,jsonfile1, jsonfile2):

    data = None
    with open(jsonfile1) as fp:
        data = json.load(fp)

    df = pd.DataFrame(columns=['Source', 'Title', 'Description', 'Content', 'URL', 'Topic'])
    '''
    ADDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
    ADD TOPIC AND COVERAGE(POS,NEG,NEUTRAL) COLUMNS
    MAYBE REMOVE CONTENT

    SEND ANOTHER REQUEST TOMORROW. 

    THERE IS A PAGE PARAMETER THAT YOU CAN USE. IT IS SET TO 1 RIGHT NOW, BUT YOU CAN CHANGE IT, set iT TO 2,3,...

    
    '''

    counter = 0
    for article in data['articles']:
        #if counter == 250:
        #    break
        source = article["source"]["name"]
        title = article["title"]
        description = article["description"]
        content = article["content"]
        url = article["url"]
        #if not df[(df['Source'] == source) & (df['Title'] == title) & (df['Description'] == description) & (df['Content'] == content) & (df['URL'] == url)].any().any():
        df = df._append({'Source': source, 'Title': title, 'Description': description, 'Content': content, 'URL':url}, ignore_index=True)
        counter+=1
        #else:
        #    continue
    '''
    with open(jsonfile2) as fp:
        data = json.load(fp)

    counter = 0
    for article in data['articles']:
        if counter == 250:
            break
        source = article["source"]["name"] 
        title = article["title"]
        description = article["description"]
        content = article["content"]
        url = article["url"]
        #if not df[(df['Source'] == source) & (df['Title'] == title) & (df['Description'] == description) & (df['Content'] == content) & (df['URL'] == url)].any().any():
        df = df._append({'Source': source, 'Title': title, 'Description': description, 'Content': content, 'URL':url}, ignore_index=True)
        counter+=1
        #else:
        #    continue

    df = df.drop_duplicates()
    '''
    df.to_excel(outfile, index=False) #much easier to read in excel

if __name__ == "__main__":
    outfile = "TS_collected_posts.xlsx"
    jsonfile1 = "Relationships1.json"
    jsonfile2 = "Eras_tour1.json"

    collect_posts(outfile,jsonfile1,jsonfile2)