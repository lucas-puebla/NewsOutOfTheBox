import facebook
import requests

def get_likes(token):
    graph=facebook.GraphAPI(access_token=token, version='2.5')
    like_raw = graph.get_object(id='me/likes')
    data=like_raw['data']
    paging=like_raw['paging']
    like_list = []
    while(True): # Wrap this block in a while loop so we can keep paginating requests until finished.
        try: # Attempt to make a request to the next page of data, if it exists and updates.
            for i in range(0,len(data)):
                like_list.append(str(data[i]['name']))
            like_raw=requests.get(paging['next']).json()
            data=like_raw['data']
            paging=like_raw['paging']
        except KeyError: # When there are no more pages (['paging']['next']), breaks
            break
    identifier='' #Creates identfier from like_list
    for i in range(0,15):
        identifier=identifier+str(like_list[i][0])
    data = open("C:/Users/Joaquin/Dropbox/Academic Chile 2016-2017/Hackathon FB/likes_text/%s.txt" %identifier, "w")
    for l in like_list: #Writes like_list
        try:
            data.write("%s\n" %l)
        except UnicodeEncodeError:
            continue
    data.close()
    print('Token read and %s likes stored in %s' %(len(like_list)-1 , identifier))
    return

#%%
token='EAACEdEose0cBAAepTzHZAi5GMDUNxgZCMoqm5uDIBhtAio13uHSuxH7HRRUKJfxvXglFkqN7Sq8ABp8WfIfY5ejt2ZBuBpjQG6odmmU7RQeijWRo1cCZATYD0uUepVx7TYnBUlYIPhxe0RjOyvHLhhhmfXplntBZA3uhWXhkCaJZA65euHMAv4'
get_likes(token)
