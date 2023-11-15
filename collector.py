
'''
Taylor swift constitutes a phrase and not a keyword: "Taylor Swift"

it's a media company that wants to know about her coverage. No time range has been
provided, but it says 'being covered in the media'. so i'm assuming we only care about
recent stuff that is relevant.
if there are enough articles, we can limit search to 2023.
Language: english

do we want to sort them? if we don't sort them in what order to they come? (exa: sortBy=popularity)

only three endpoints available, we will use /v2/everything

We won't get all 500 articles from a single query. we want to look at multiple keywords that belong to different categories/topics.
We will send multiple requests, each looking for articles that highlight a specific topic about taylor swift.

From these, we take a random sample 500 articles (in a way that one topic isn't over-represented.)

'''

from pathlib import Path
from requests import get
import datetime
import json

query_string = 'https://newsapi.org/v2/everything?'

#On Windows it seems like you basically can't use os.environ to extract environment variables from your .env file.
#therefore I used this method instead.
def get_APIKEY():
    env_file = Path('.env')

    with open(env_file) as fp:
        return fp.read()
    

# make sure you surround phrases with ""
# i'll also include the topic column for the saved data, but we'll probably have to change its values later
def fetch_latest_news(api_key, news_keywords, topic):

    current_date = datetime.date.today()
    lookback = datetime.date.today() - datetime.timedelta(31)

    #might have to edit this to have +keywOR+keyw+...
    edited_keyword = []
    for i in range(len(news_keywords)):
        if i!=0:
            edited_keyword.append('AND')
        if ' ' in news_keywords[i]:
            #phrases are sentences that contain whitespace, and they need to be surrounded by quotes in the query string
            news_keywords[i] = f'"{news_keywords[i]}"' 
        edited_keyword.append(news_keywords[i])
    edited_keyword = ''.join(edited_keyword)

    query = f'{query_string}q={edited_keyword}&from={str(lookback)}&to={str(current_date)}&apiKey={api_key}'
    
    #print(query)
    response = get(query)
    response = response.json()

    #return response
    with open(f"{topic}.json", "w") as fp:
        json.dump(response, fp, indent=4)
    

if __name__ == "__main__":
    #The topics that we want to explore
    taylor_swift_eras_tour = ['+Taylor Swift', 'The Eras Tour', 'The Eras Tour Concert Film']

    taylor_swift_drama = ['+Taylor Swift', 'Kanye West', 'Katy Perry', 'Scooter Braun']

    taylor_swift_relationships = ['+Taylor Swift', 'Calvin Harris', 'Joe Alwyn', 'Travis Kelce', 'Tom Hiddleston', 'Harry Styles']

    taylor_swift_acting = ['+Taylor Swift', 'Movie', 'Acting']

    #a problem with these keywords is that they're album names, but might get misinterpreted for something else
    taylor_swift_music = ['+Taylor Swift', 'music', 'discography', 'Midnights', 'Speak Now', '1989', 'Lover', 'repuration', 'Fearless', 'Red', 'Folklore', 'Evermore', 'concert']

    taylor_swift_bio = ['+Taylor Swift', 'Career', 'Legacy', 'Cultural Status', 'image', 'Early Life', 'Biography']

    taylor_swift_politics = ['+Taylor Swift', 'Politics', 'Feminism', 'Activism', 'Democrat', "LGBTQ", 'Advocacy', 'COVID-19', 'Social Media', 'Philantropy']

    key = get_APIKEY()

    #res = fetch_latest_news(key, taylor_swift_eras_tour, 'Eras Tour')

    #with open("res.json", "w") as fp:
    #    json.dump(res, fp, indent=4)

    research_list = [(taylor_swift_eras_tour, "Eras_Tour") \
                     , (taylor_swift_drama, "Drama") \
                     ,(taylor_swift_acting, "Movies") \
                     ,(taylor_swift_relationships, "Relationships") \
                     ,(taylor_swift_music, "Music") \
                     ,(taylor_swift_bio, "Biography") \
                     ,(taylor_swift_politics, "Politics")]


    for research_tuple in research_list:
        fetch_latest_news(key, research_tuple[0], research_tuple[1])

    '''
    - We haven't limited our search to North America. Not sure how we can do this programmatically, since there is no country/region parameter for the 
    query string. Best we can do is to use the language parameter and set it to English (en). I think we'll have to filter articles that aren't from North
    America manually.
    - The same article can appear in multiple response JSONs, we have to filter them out.
    - For sampling, we can use the  sortBy= parameter to get the most relevant stuff, and then do systemic sampling by ID. (adding them one by one to our final csv/tsv file).
    - the JSON responses will have different sizes, we'll have to make sure the number of articles selected from each is proportionate to their size.
    I don't see how picking randomly from each JSON will increase the representativeness of our sample
    '''