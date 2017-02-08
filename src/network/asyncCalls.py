import aiohttp
import asyncio
import json
import signal
import sys
import asyncClass

loop = asyncio.get_event_loop()
networkClass = asyncClass.asyncClass(loop=loop)
# client = aiohttp.ClientSession(loop=loop)
#
# async def get_json(client, url):
#     async with client.get(url) as response:
#         assert response.status == 200
#         return await response.read()
#
# async def get_output(client,url,headers):
#     async with client.get(url,headers=headers) as response:
#         if response.status == 200:
#             return await response.read()
#         else:
#             return response.status
#
#
# async def get_reddit_top(subreddit, client):
#     data1 = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')
#
#     j = json.loads(data1.decode('utf-8'))
#     for i in j['data']['children']:
#         score = i['data']['score']
#         title = i['data']['title']
#         link = i['data']['url']
#         print(str(score) + ': ' + title + ' (' + link + ')')
#
#     print('DONE:', subreddit + '\n')

def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


asyncio.ensure_future(networkClass.get_reddit_top('python'))
asyncio.ensure_future(networkClass.get_reddit_top('android'))
asyncio.ensure_future(networkClass.get_reddit_top('ios'))
asyncio.ensure_future(networkClass.get_zomatoCategories())
loop.run_forever()