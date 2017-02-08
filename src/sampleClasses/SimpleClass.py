import asyncio
import aiohttp
import json

class TitleSong(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_song(self):
        for line in self.lyrics:
            print (line)

class CityEnCoder(json.JSONEncoder):
    def default(self,obj):
        obj["id"] = int(obj["id"])
        obj["name"] = obj["name"]
        obj["country_id"] = int(obj["country_id"])
        obj["country_name"] = obj["country_name"]
        obj["discovery_enabled"] = int(obj["discovery_enabled"])
        obj["has_new_ad_format"] = int(obj["has_new_ad_format"])
        obj["is_state"] = obj["is_state"]
        obj["state_id"] = obj["state_id"]
        obj["state_name"] = obj["state_name"]
        obj["state_code"] = obj["state_code"]
        return super(CityEnCoder,self).encode(obj)

# class suggested_cities(json.JSONEncoder):
#     def default(self,obj):
#         if isinstance(obj,list):

class NetworkSong(object):

    def __init__(self,loop):
        self.loop = loop

    async def get_json(self,url,session):
        async with session.get(url) as response:
            assert response.status == 200
            return await response.read()

    async def get_json_headers(self,url,headers,session):
        async with session.get(url,headers=headers) as response:
            if response.status == 200:
                return await response.read()
            else:
                return response.status

    async def get_json_headers_parameters(self,url,parameters,headers,session):
        async with session.get(url=url,headers=headers,params=parameters) as response:
            if response.status == 200:
                return await response.read()
            else:
                return response.status

    async def printJson(self,url,session):
        data1 = await self.get_json(url=url,session=session)
        print(data1.decode('utf-8'))

    async def printZomatoCategories(self,url,session,header):
        data1 = await self.get_json_headers(url=url,headers=header,session=session)
        j = json.loads(data1.decode('utf-8'))
        for i in j["categories"]:
            print(i["categories"]["id"],"-",i["categories"]["name"])

    async def printZomatoCities(self,url,headers,params,session):
        data1 = await self.get_json_headers_parameters(url=url,parameters=params,headers=headers,session=session)
        # return data1.decode('utf-8')
        json_string = json.loads(data1.decode('utf-8'))
        print (json_string['has_total'])
        for i in json_string['location_suggestions']:
            print (i['name'])

    # getting the Zomato Cities
    async def getZomatoCities(self,url,headers,params,session):
        data1 = await self.get_json_headers_parameters(url=url,parameters=params,headers=headers,session=session)
        return data1.decode('utf-8')

