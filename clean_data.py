import json
import pandas as pd

def cleanup_code():
    file = "FINAL_DATA.xlsx"

    df = pd.read_excel(file)

    #df = df.drop_duplicates(subset=["Source", "Title", "Description", "Content", "URL"])

    #print(df)

    topics = {'Movie':0, 'Music':0, 'Concerts':0, 'Personal Life':0, 'Culture':0}
    coverage = {'Positive':0, 'Negative':0, 'Neutral':0}

    for index, row in df.iterrows():
        topics[row['Topic']]+=1
        coverage[row['Coverage']]+=1
        '''if row['Topic']=='personal' or row['Topic']=='Personal/Private Life':
            df.at[index, 'Topic'] = 'Personal Life'
        if row['Topic']=='tour' or row['Topic']=='Tours/Concerts':
            df.at[index, 'Topic'] = 'Concerts' '''
        '''if row['Topic'] not in topics:
            print("wrong topic", index)
        if row['Coverage'] not in coverage:
            print("Wrong coverage", index)'''

    topics_total = 0
    coverage_total = 0 # both of these should sum up to 500
    for topic in topics:
        topics_total+=topics[topic]
    for cover in coverage:
        coverage_total+=coverage[cover]
    
    print("topics total", topics_total)
    print("coverage total", coverage_total)
    #df.to_excel("FINAL_DATA.xlsx", index=False)

if __name__ == "__main__":
    pass