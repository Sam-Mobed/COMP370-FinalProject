
'''
Taylor swift constitutes a phrase and not a keyword: "Taylor Swift"

it's a media company that wants to know about her coverage. No time range has been
provided, but it says 'being covered in the media'. so i'm assuming we only care about
recent stuff that is relevant.
if there are enough articles, we can limit search to 2023.
Language: english

do we want to sort them? if we don't sort them in what order to they come? (exa: sortBy=popularity)

only three endpoints available, we will use /v2/everything

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
def fetch_latest_news(api_key, news_keywords, topic, page_num):

    current_date = datetime.date.today()
    lookback = datetime.date.today() - datetime.timedelta(31)

    #might have to edit this to have +keywOR+keyw+...
    edited_keyword = []
    for i in range(len(news_keywords)):
        if i!=0:
            edited_keyword.append('OR')
        if ' ' in news_keywords[i]:
            #phrases are sentences that contain whitespace, and they need to be surrounded by quotes in the query string
            news_keywords[i] = f'"{news_keywords[i]}"' 
        edited_keyword.append(news_keywords[i])
    edited_keyword = ''.join(edited_keyword)

    #query = f'{query_string}q={edited_keyword}&sortBy=relevancy&excludeDomains=*.uk&language=en&from={str(lookback)}&to={str(current_date)}&apiKey={api_key}'
    #three changes I made, I used OR to join keywords, I set language=en and sorted by relevancy,
    #query = f'{query_string}q={edited_keyword}&sortBy=relevancy&excludeDomains=*.uk,*.fr,*.de,*.es,*.ru&language=en&from={str(lookback)}&to={str(current_date)}&apiKey={api_key}'
    query = f'{query_string}q={edited_keyword}&sortBy=relevancy&excludeDomains=*.uk,*.fr,*.de,*.es,*.ru&page={page_num}&language=en&from={str(lookback)}&to={str(current_date)}&apiKey={api_key}'
    '''
    the media company says that they are especially concerned with North American coverage. this doesn't mean that they ONLY want north american coverage,
    just mostly. But what I can do is either only include NA coverage, or all english coverage.
    i think the best comprompise we can do is use the * wildcard to filter out all *.uk, *.fr, etc. websites. This will filter out sites that are not obviously 
    North American, but we will still have sites like BBC News (which is English). 
    This is probably the best way to get mostly get NA coverage without completely excluding other sources.
    '''
    #print(query)
    response = get(query)
    response = response.json()

    #return response
    with open(f"{topic}_{page_num}.json", "w") as fp:
        json.dump(response, fp, indent=4)
    

if __name__ == "__main__":
    #The topics that we want to explore
    taylor_swift_eras_tour = ['+Taylor Swift', 'The Eras Tour', 'The Eras Tour Concert Film']

    #taylor_swift_drama = ['+Taylor Swift', 'Kanye West', 'Katy Perry', 'Scooter Braun']
    #she has no recent drama, and the people listed are drama from a long time ago, thus we don't get any articles related to their beef.
    #taylor_swift_relationships = ['+Taylor Swift', 'Calvin Harris', 'Joe Alwyn', 'Travis Kelce', 'Tom Hiddleston', 'Harry Styles']
    #the only recent boyfriend she has is Travis Kelce, I haven't seen a single Article about the other people, so we can just ignore them
    taylor_swift_relationships = ['+Taylor Swift', '+Travis Kelce']

    #taylor_swift_acting = ['+Taylor Swift', 'Movie', 'Acting', 'Film']

    #a problem with these keywords is that they're album names, but might get misinterpreted for something else
    #taylor_swift_music = ['+Taylor Swift', 'music', 'discography', 'Midnights', 'Speak Now', '1989', 'Lover', 'repuration', 'Fearless', 'Red', 'Folklore', 'Evermore', 'concert']

    #taylor_swift_bio = ['+Taylor Swift', 'Career', 'Legacy', 'Cultural Status', 'image', 'Early Life', 'Biography']

    #taylor_swift_politics = ['+Taylor Swift', 'Politics', 'Feminism', 'Activism', 'Democrat', "LGBTQ", 'Advocacy', 'COVID-19', 'Social Media', 'Philantropy']

    key = get_APIKEY()

    #res = fetch_latest_news(key, taylor_swift_eras_tour, 'Eras Tour')

    #with open("res.json", "w") as fp:
    #    json.dump(res, fp, indent=4)
    '''
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
    research_list = [(taylor_swift_eras_tour, "Eras_Tour1"),(taylor_swift_relationships, "Relationships1")]

    for research_tuple in research_list:
        for i in range(1,6):
            fetch_latest_news(key, research_tuple[0], research_tuple[1], i)

    '''
    - We haven't completely limited our search to North America. But we made sure that the articles are in English, the main language spoken in Canada and in the US,
    and we excluded obvious domains like *.fr, *.uk, etc. => BBC.co.uk is included, so im not sure this worked properly. The response objects looked fine so idk.
    If we really want to limit coverage from outside NA, we can use domains= parameter.
    - The same article can appear in multiple response JSONs, I made sure to filter them out.
    - For sampling, we used the  sortBy= parameter to get the most relevant stuff, and then did systemic sampling by ID. (adding them one by one to our final csv/tsv file).
    - the JSON responses will have different sizes, we'll have to make sure the number of articles selected from each is proportionate to their size.
    I don't see how picking randomly from each JSON will increase the representativeness of our sample
    - sometimes, the article is not about taylor swift, but it seems like she gets mentioned in one of the ads and the APi still counts it as mentioning Taylor.
    - sometimes, Taylor isn't directly mentioned in title, content or description. click on the link to see if she's mentioned in the whole article (ctrl+F), (apparently this is unnecessary)
    - For articles that are completely unrelated to Taylor Swift, highlight them in red, and we will exclude them from the Final Dataset.
    '''