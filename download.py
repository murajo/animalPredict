from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
from settings_sercret import *
import os, time, sys

# APIキーの登録
key = KEY
sercret = SERCRET
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = "image/" + animalname

flickr = FlickrAPI(key, sercret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
# pprint(photos)

for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
