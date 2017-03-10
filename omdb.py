import omdb, json
import requests
import time
import codecs
from pymongo import MongoClient

url = 'http://www.omdbapi.com/?'

#http://www.omdbapi.com/?t=%22the+salesman%22&y=&plot=short&r=json

def load_movie_list():
    movie_list = []
    movie_file_name = 'movies_imdb.txt' 
    with open(movie_file_name) as f:
        content = f.readlines()
        movie_list = [x.strip() for x in content]
    return movie_list

def setup_mongodb():
    try:        
        client = MongoClient('localhost', 27017)
        db = client['CS540_db']
        collection = db['imdb_collection']
        return collection
    except BaseException, e:
        print 'failed on database connection', str(e)
        pass

movie_list = load_movie_list()
collection = setup_mongodb()
for i, movie  in enumerate(movie_list):
    parameters = dict(t=movie)
    resp = requests.get(url=url, params=parameters)
    data = json.loads(resp.text)
    if 'Title' in data:
        with open('imdb_movies.json', 'a') as outfile:
            json.dump(data, codecs.getwriter('utf-8')(outfile), ensure_ascii=False)
            outfile.write('\n')
            collection.insert(data)

        print i+1, data['Title']
    else:
        with open('imdb_movies_not_found.txt', 'a') as notfound:
            notfound.write(movie+'\n')
    time.sleep(1)