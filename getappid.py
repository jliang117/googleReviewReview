import play_scraper as ps
# COLLECTIONS = {
#     'NEW_FREE': 'topselling_new_free',
#     'NEW_PAID': 'topselling_new_paid',
#     'TOP_FREE': 'topselling_free',
#     'TOP_PAID': 'topselling_paid',
#     'TOP_GROSSING': 'topgrossing',
#     'TRENDING': 'movers_shakers',
# }

#Categories: https://github.com/danieliu/play-scraper/blob/master/play_scraper/lists.py#L12

STORE_APPID_KEY = 'app_id'

#return collection as list of app ids
def returnAppIds(foundCollection):
	appIds = []
	for col in foundCollection:
		appIds.append(col[STORE_APPID_KEY])
	return appIds

def getIdList(collectionType, numResults = None, category = None):
	if(numResults is None):
		numResults = 1
	return returnAppIds(ps.collection(collection=collectionType,results=numResults,category=category))

# usage print(getIdList('TRENDING',100))