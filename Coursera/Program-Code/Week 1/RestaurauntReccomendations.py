def reccomend(file, price, cuisines_list):
    
 
def read_restaurant(file):
    """(file) -> (dict, dict, dict)
    #dict of {str: int}
    name_to_rating = {'Georgie Porgie': 87, 'Queen St. Cafe': 82,
		  'Dumplings R Us': 71, 'Mexican Grill': 85,
		  'Deep Fried Everything': 52}
    #dict of {str: list of str}
    price_to_names = {'$': ['Queen St. Cafe', 'Dumplings R Us',
                        'Deep Fried Everything'],
                  '$$': ['Mexican Grill'],
                  '$$$': ['Georgie Porgie'],
                  '$$$$': []}
    #dict of {str: list of str}
    cusine_to_names = {'Canadian': ['Georgie Porgie'],
                   'Pub Food': ['Georgie Porgie'],
                   'Malasyian': ['Queen St. Cafe'],
                   'Thai': ['Queen St. Cafe'],
                   'Chinese': ['Dumplings R Us'],
                   'Mexican': ['Mexican Grill']}
    """
    name_to_rating = {}
    price_to_names = {'$':[], '$$':[], '$$$':[], '$$$$':[]}
    cuisine_to_names = {}
    
