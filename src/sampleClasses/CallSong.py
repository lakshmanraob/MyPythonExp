import SimpleClass
import asyncio
import aiohttp
import signal
import sys
import json

titleSong = SimpleClass.TitleSong(["call one","call two"])
titleSong.sing_me_song()

mZHeaders = {'user-key':'292a37cc09bcbc708e32503f219bb9c3'}
mZCategories = "https://developers.zomato.com/api/v2.1/categories"
mZCities = "https://developers.zomato.com/api/v2.1/cities"

loop = asyncio.get_event_loop()
session = aiohttp.ClientSession(loop=loop)

networksong = SimpleClass.NetworkSong(loop=loop)

# def signal_handler(signal, frame):
#     loop.stop()
#     session.close()
#     sys.exit(0)
#
# signal.signal(signal.SIGINT, signal_handler)


# asyncio.ensure_future(networksong.printJson('https://www.reddit.com/r/python/top.json?sort=top&t=day&limit=5',session=session))
# asyncio.ensure_future(networksong.printZomatoCategories(url=mZCategories,session=session,header=mZHeaders))
# loop.run_forever()

print("------ Restauarnt Search ----")
searchkey = input("Enter your area's first three letters")
print("possible suggestions are ....")
params = {'q':searchkey}
# asyncio.ensure_future(networksong.printZomatoCities(url=mZCities,headers=mZHeaders,params=params,session=session))
try:
    task_obj = loop.create_task(networksong.getZomatoCities(url=mZCities,headers=mZHeaders,params=params,session=session))
    # loop.run_forever()
    loop.run_until_complete(task_obj)
finally:
    loop.close()

json_string = json.loads(task_obj.result())

suggestedCityList = json_string['location_suggestions']

selectedCity = int(input("select the city"))

print("selected city name :",suggestedCityList[selectedCity]["name"])
print("selected object value is ",suggestedCityList[selectedCity])