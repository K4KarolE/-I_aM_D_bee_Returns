import requests
import json

link = 'https://www.imdb.com/title/tt7366338/?ref_=adv_li_tt' # Csernobil
link = 'https://www.imdb.com/title/tt0106697/?ref_=nv_sr_srsg_0' # Pusztito
link_split= link.split('/')

for i in link_split:
    if i[0:2] == 'tt':
        imdb_id = i

api_key = ''

# FIND TITLE
link_find = f'https://api.themoviedb.org/3/find/{imdb_id}?api_key={api_key}&language=en-US&external_source=imdb_id'
response = requests.get(link_find)


# SAVE, LOAD 'FIND TITLE' RESPONSE
with open('find_title.json', 'w') as f:
    json.dump(response.json(), f, indent=2)

f = open('find_title.json')
title_dic = json.load(f)

# MOVIE VS. TV - MEDIA DECIDER
if title_dic['movie_results'] != []:
    title_dic_active = 'movie_results'
else:
    title_dic_active = 'tv_results'

title = title_dic[title_dic_active][0]["title"]
original_title = title_dic[title_dic_active][0]["original_title"]
id = title_dic[title_dic_active][0]["id"]
media_type = title_dic[title_dic_active][0]["media_type"] # movie / tv

print(title, original_title, id, media_type)