import asyncio
import aiohttp
import json
import signal
import sys

class asyncClass:

    def __init__(self,loop):
        session = aiohttp.ClientSession(loop=loop)

    # for getting the values from the reddit website
    async def get_reddit_top(self,subreddit):
        data1 = get_json(url='https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')
        j = json.loads(data1.decode('utf-8'))
        for i in j['data']['children']:
            score = i['data']['score']
            title = i['data']['title']
            link = i['data']['url']
            print(str(score) + ': ' + title + ' (' + link + ')')
        print('DONE:', subreddit + '\n')


    # for getting the categories from zomato
    async def get_zomatoCategories(self):
        print("inside the class to accept get the values")
        murl = "https://developers.zomato.com/api/v2.1/categories"
        mparams = {'user-key':'292a37cc09bcbc708e32503f219bb9c3'}
        data1 = get_json_with_parameters(url=murl,headers=mparams)
        j = json.loads(data1.decode('utf-8'))
        for i in j["categories"]:
            print(i["categories"]["id"],"-",i["categories"]["name"])
        print (data1)


    async def get_json(self,url):
        async with session.get(url) as response:
            assert response.status == 200
            return await response.read()


    async def get_json_with_parameters(self,url,headers):
        async with session.get(url,headers=headers) as response:
            if response.status == 200:
                return await response.read()
            else:
                return response.status









