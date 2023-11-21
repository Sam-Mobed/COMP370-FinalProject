import argparse
import json
import pandas as pd

def parse_text(text):
    #parses text to make sure that title/description of article mentions Taylor Swift, Travis, Eras,...
    #don't think we'll need this, should be very few articles that are unrelated, can be done by hand.
    #otherwise, come back here and use regex
    pass
'''
def collect_posts(outfile,jsonfile1):

    data = None
    with open(jsonfile1) as fp:
        data = json.load(fp)

    df = pd.DataFrame(columns=['Source', 'Title', 'Description', 'Content', 'URL', 'Topic', 'Coverage'])

    for article in data['articles']:
        source = article["source"]["name"]
        title = article["title"]
        description = article["description"]
        content = article["content"]
        url = article["url"]
        df = df._append({'Source': source, 'Title': title, 'Description': description, 'Content': content, 'URL':url, 'Topic': "None", 'Coverage': "None"}, ignore_index=True)

    df = df.drop_duplicates()
    
    df.to_excel(outfile, index=False) #much easier to read in excel
'''
def add_to_excel(json_list, excel_file):
    
    
    #df = pd.read_excel(excel_file)

    df = pd.DataFrame(columns=['Source', 'Title', 'Description', 'Content', 'URL', 'Topic', 'Coverage'])

    for jsonfile in json_list:
        data = None
        with open(jsonfile) as fp:
            data = json.load(fp)

        for article in data['articles']:
            source = article["source"]["name"] 
            title = article["title"]
            description = article["description"]
            content = article["content"]
            url = article["url"]
            df = df._append({'Source': source, 'Title': title, 'Description': description, 'Content': content, 'URL':url, 'Topic': "None", 'Coverage': "None"}, ignore_index=True)

    df = df.drop_duplicates()

    df.to_excel(excel_file, index=False)

if __name__ == "__main__":
    outfile = "TS_collected_posts.xlsx"

    #collect_posts(outfile,jsonfile1)

    #I used to have all of these inside the same folder, I moved them, these have to be edited to have their proper path
    json_list = ['page1.json','page2.json','page3.json','page4.json','page5.json','page6.json','page7.json']

    add_to_excel(json_list, outfile)