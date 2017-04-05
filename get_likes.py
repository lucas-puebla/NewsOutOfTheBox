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
    #Writes like_list
    data = open("C:/Users/Joaquin/Dropbox/Academic Chile 2016-2017/Hackathon FB/likes_text/%s.txt" %identifier, "w")
    for l in like_list:
        try:
            data.write("%s\n" %l)
        except UnicodeEncodeError:
            continue
    data.close()
    return

token='EAACEdEose0cBABivOhD4ItVRRavVOC1rvJYqZBYy01QVgmjEuEq2qNmtv1kUcrGhZChxQIESTMWGrjeS2QYw28dRHGdiTC49hdEVGXcSNI08CelKjtynapXx5VmyfHHS5dZBXtn8C3ZAIEyi0qSi3DbQZCe7DJuJYpfA0kLkwu9NSGZCYRZBzdw'
get_likes(token)
