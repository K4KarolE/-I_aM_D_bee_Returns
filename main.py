import requests
import json

# API KEY
api_key = open('api_key.txt').read()

# GET LINK / IMDB ID - will be from clipboard
link = 'https://www.imdb.com/find/tt7366338/?ref_=adv_li_tt' # Chern. - TV
# link = 'https://www.imdb.com/find/tt0106697/?ref_=nv_sr_srsg_0' # Dem. man
# link = 'https://www.imdb.com/title/tt0120855/?ref_=nv_sr_srsg_0' # Tarzan - multiple directors
link_split= link.split('/')

for i in link_split:
    if i[0:2] == 'tt':
        imdb_id = i

## FIND
link_find = f'https://api.themoviedb.org/3/find/{imdb_id}?api_key={api_key}&language=en-US&external_source=imdb_id'
response = requests.get(link_find)

# SAVE, LOAD 'FIND TITLE' RESPONSE
with open('find.json', 'w') as f:
    json.dump(response.json(), f, indent=2)

f = open('find.json')
find_dic = json.load(f)

# MOVIE VS. TV - MEDIA DECIDER
if find_dic['movie_results'] != []:
    find_dic_active = 'movie_results'
    title_name = 'title'
    title_name_original = 'original_title'
else:
    find_dic_active = 'tv_results'
    title_name = 'name'
    title_name_original = 'original_name'

title = find_dic[find_dic_active][0][title_name]
original_title = find_dic[find_dic_active][0][title_name_original]
id = find_dic[find_dic_active][0]["id"]
media_type = find_dic[find_dic_active][0]["media_type"] # movie / tv

if title != original_title:
    title = f'{title}\n({original_title})'


### DETAILS
link_details = f'https://api.themoviedb.org/3/{media_type}/{id}?api_key={api_key}&language=en-US'
response = requests.get(link_details)


# SAVE, LOAD 'DETAILS' RESPONSE
with open('details.json', 'w') as f:
    json.dump(response.json(), f, indent=2)

f = open('details.json')
details_dic = json.load(f)
# GENRES
genres = []
for item in details_dic['genres']:
    genres.append(item['name'])
# RELEASE YEAR
if media_type == 'movie':
    year_of_release = details_dic['release_date'][0:4]
else:
    first_air_date = details_dic['first_air_date'][0:4]
    last_air_date = details_dic['last_air_date'][0:4]
    if last_air_date == [] or first_air_date == last_air_date:
        year_of_release = first_air_date
    else:
        year_of_release = f'{first_air_date}-{last_air_date}'
# RUNTIME
if media_type == 'movie':
    runtime = details_dic['runtime']
else:
    runtime = details_dic['episode_run_time'][0]
hour = int(runtime/60)
minutes = runtime%60



### CREDITS
link_credits = f'https://api.themoviedb.org/3/{media_type}/{id}/credits?api_key={api_key}&language=en-US'
response = requests.get(link_credits)

# SAVE, LOAD 'CREDITS' RESPONSE
with open('credits.json', 'w') as f:
    json.dump(response.json(), f, indent=2)

f = open('credits.json')
credits_dic = json.load(f)

# ACTORS
actors = []
i = 0
while i < 3:
    actors.append(credits_dic['cast'][i]["name"])
    i += 1

# DIRECTORS
if media_type == 'movie':
    directors = []
    for item in credits_dic['crew']:
            if item["job"] == "Director":
                directors.append(item["name"])


### IMAGES
link_images = f'https://api.themoviedb.org/3/{media_type}/{id}/images?api_key={api_key}'
response = requests.get(link_images)

#SAVE, LOAD 'CREDITS' RESPONSE
with open('images.json', 'w') as f:
    json.dump(response.json(), f, indent=2)

f = open('images.json')
images_dic = json.load(f)

posters = []
for item in images_dic["posters"]:
    if item["iso_639_1"] == "en":
        posters.append(item["file_path"])


poster_links = []
for item in posters:
    poster_links.append(f'https://image.tmdb.org/t/p/w200{item}')

for i in poster_links:
    print(i)
