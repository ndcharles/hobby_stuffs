# You can download the individual rate cards and find the country to region mapping for countries where regional rates apply.
# Given the Facebook cost per conversion in USD sheet, get a dictionary with key: value pairs.
# Market : Business-Initiated Rate, User-Initiated Rate 
# https://developers.facebook.com/docs/whatsapp/pricing

# I like this Stanford tuts on python dictionary
# http://www.compciv.org/guides/python/fundamentals/dictionaries-overview/
# Instagram Basic display API: https://developers.facebook.com/docs/instagram-basic-display-api
# 

'''
cost = "market" : {
    "Argentina" : [0.0526, 0.0316],
    "Brazil" : [0.0500, 0.0300],
    "Chile" : [0.0757, 0.0454],
    "Nigeria" : [0.0516, 0.0310]
}

for key, value in enumertae():
    print(key, value)



datathing = {
  "status": "good",
  "last_updated": "2012-12-07T18:11:55Z"
}

if datathing['status'] == 'good':
    print("Things are good")
else: 
    print("WTF!?!??!")

****

datathing = [{
    "status": "good",
    "body": "Everything operating normally.",
    "created_on": "2016-01-21T20:28:31Z"
}, {
    "status": "minor",
    "body": "We're investigating issues serving GitHub pages.",
    "created_on": "2016-01-21T20:25:03Z"
}, {
    "status": "good",
    "body": "Everything operating normally.",
    "created_on": "2016-01-20T22:56:57Z"
}, {
    "status": "minor",
    "body": "We're investigating issues affecting a small number of repositories.",
    "created_on": "2016-01-20T22:47:07Z"
}]


for d in datathing: # remember that datathing is a list
    print(d['created_on'], '--',
        d['status'] + ':')
    print(d['body'])
    print("")

****

#snoop dogg on instagram 
datathing = {
      "data": {
          "id": "1574083",
          "username": "snoopdogg",
          "full_name": "Snoop Dogg",
          "profile_picture": "http://distillery.s3.amazonaws.com/profiles/profile_1574083_75sq_1295469061.jpg",
          "bio": "This is my bio",
          "website": "http://snoopdogg.com",
          "counts": {
              "media": 1320,
              "follows": 420,
              "followed_by": 3410
          }
  }
}

user = datathing["data"]
print(user['username'])
print("Bio:", user["bio"])

counts = user['counts']
print("You follow this number of people:", counts['follows'])

*****
'''

# beyonce on spotify 
beyonce = {
  "name" : "Beyonce",
  "popularity" : 86,
  "type" : "artist",
  "uri" : "spotify:artist:6vWDO969PvNqNYHIOW5v0m",
  "external_urls" : {
    "spotify" : "https://open.spotify.com/artist/6vWDO969PvNqNYHIOW5v0m"
  },
  "followers" : {
    "href" : None,
    "total" : 3841151
  },
  "genres" : [ "dance pop", "pop", "r&b", "urban contemporary" ],
  "href" : "https://api.spotify.com/v1/artists/6vWDO969PvNqNYHIOW5v0m",
  "id" : "6vWDO969PvNqNYHIOW5v0m",
  "images" : [ {
    "height" : 1000,
    "url" : "https://i.scdn.co/image/a370c003642050eeaec0bc604409aa585ca92297",
    "width" : 1000
  }, {
    "height" : 640,
    "url" : "https://i.scdn.co/image/79e91d3cd4a7c15e0c219f4e6c941d282fe87a3d",
    "width" : 640
  } ]
}

# get her actual name
print(beyonce['name'])

# get her number of followers
print(beyonce['followers']['total'])

# get the genres
print(beyonce["genres"])

# get the images she has, with their attributes
for img in beyonce['images']:
     print('-----')
     for key, val in img.items():
         print(key + ':', val)