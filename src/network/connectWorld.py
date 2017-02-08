import httplib2
import json

# h = httplib2.Http(".cache")
# resp, content = h.request('http://www.google.com/', "GET")

print(httplib2.__version__);

# url = "https://developers.zomato.com/api/v2.1/categories"
# headers = "{'user-key':292a37cc09bcbc708e32503f219bb9c3,'accept':application/json,'cache-control':no-cache}"
#
h = httplib2.Http()
response2, content2 = h.request('https://developers.zomato.com/api/v2.1/categories',method='GET',
                                headers={'user-key':'292a37cc09bcbc708e32503f219bb9c3'})
# response2, content2 = h.request(url,headers)
parsed_json = json.loads(content2.decode('utf-8'))
print (parsed_json["categories"])
# print (content2.decode('utf-8'))
print (response2.status)
print (dict(response2.items()))