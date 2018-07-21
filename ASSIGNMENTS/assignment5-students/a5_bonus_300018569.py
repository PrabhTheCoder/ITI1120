#Family name: Tara
# Student number: 300018569
# Course: IT1 1120 
# Assignment Number: 5
class Person:

    # YOUR CODE GOES HERE
    def __init__(self, uid, name, friends = []):
        """(Person, int, string, list of int) -> None"""
        self.id = uid
        self.name = name
        self.friends = friends[:]

    def __repr__(self):
        """(Person) -> str"""
        return "Person({},{},{})".format(self.id, self.name, self.friends)
    def get_friends(self):
        """(Person) -> list"""
        return self.friends
    def add_friend(self, uid):
        """(Person, int) -> None"""
        self.friends.append(uid)
class Network:
    # YOUR CODE GOES HERE
    def __init__(self, name_file, id_file):
        """(Network, str, str) -> None"""
        self.network = []
        n_f = open(name_file).read().splitlines()
        friends = open(id_file).read().splitlines()

        for query in n_f:
            id_name = query.split("\t")
            self.network.append(Person(int(id_name[0]), id_name[1]))

        del friends[0]
        
        
        for i in range(len(friends)):
            nums = friends[i].split(" ")
            curr_id = int(nums[0])
            connection = int(nums[1])
            friends[i] = [curr_id,connection]


        for i in range(len(friends)): 
            curr_user = friends[i][0]
            connection = friends[i][1]
            id_user = self.search_id(curr_user)
            id_conn = self.search_id(connection)
            self.network[id_user].add_friend(connection)
            self.network[id_conn].add_friend(curr_user)


    def __repr__(self):
        """(Network) -> str"""
        return "Network({})".format(self.network)


    def __len__(self):
        """(Network) -> int"""
        return len(self.network)


    def recommend(self, user):
        """(Network, int)->int or None"""
        user_friends = self.network[self.search_id(user)].get_friends()
        user_friends = set(user_friends)
        candidates = {p.id for p in self.network}
        candidates = candidates - user_friends
        candidates = candidates - {user}
        recommended = [0]
        
        for candidate in candidates:
            num = len(self.getCommonFriends(user, candidate))
            if num > 0:
                if len(recommended) != 2:
                    recommended[0] = candidate
                    recommended.append(num)
                if num > recommended[1] or num == recommended[1] and recommended[0] > candidate:
                    recommended.pop()
                    recommended.pop()
                    recommended.append(candidate)
                    recommended.append(num)

                
        if len(recommended) == 2:
            return recommended[0]


    def getCommonFriends(self, user1, user2):
        """(Network, int, int) -> list"""
        common=[]
        
        friends_of_user1 = self.network[self.search_id(user1)].get_friends()
        friends_of_user2 = self.network[self.search_id(user2)].get_friends()
        index_user1 = 0
        index_user2 = 0

        while index_user1 < len(friends_of_user1) and index_user2 < len(friends_of_user2):
            if friends_of_user1[index_user1] < friends_of_user2[index_user2]:
                index_user1 += 1
            elif friends_of_user2[index_user2] < friends_of_user1[index_user1]:
                index_user2 += 1
            else:
                common.append(friends_of_user1[index_user1])
                index_user1 += 1
                index_user2 += 1

        return common

    def get_uid(self):
        """(Network)->int"""

        index = -1
        
        while index == -1:
            
            try:
                uid = int(input("Enter an integer for a user ID: ").strip())
                index = self.search_id(uid)
                
                if index == -1:
                    print("That user ID does not exist. Try again")
                    
            except ValueError:
                print("That was not an integer. Please try again.")
                
        return uid

    def search_id(self, value):
        """(Network, int) -> int"""
        
        end = len(self.network) -1
        begin = 0
        
        while end - begin > 1:
            mid = (end+begin)//2
            key = self.network[mid].id
            if key < value:
                begin = mid + 1
            elif key > value:
                end = mid - 1
            else: #foundit
                return mid
        if self.network[begin].id == value:
            return begin
        elif self.network[end].id == value:
            return end
        
        return -1    

        
            


def get_int():
    '''None->int or None'''
    num = None
    try:
        num=int(input("Enter an integer for a user ID:").strip())
    except ValueError:
        print("That was not an integer. Please try again.")
    return num           

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name
    
    

##############################
# main
##############################
print("Let's get first file that contains IDs and names:")
file_name1=get_file_name()
print("Let's get the 2nd file that contains pairs of friends as in Assignment 4")
file_name2=get_file_name()


net=Network(file_name1,file_name2)
print("Here are all the people in the network, if the network has at most 20 users:")
if len(net)<=20:
    print(net)


print("\nLet's recommend a friend for a user you specify.")
uid=net.get_uid()
rec=net.recommend(uid)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(net.getCommonFriends(uid,rec)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=net.get_uid()
print("About 2st user ...")
uid2=net.get_uid()
print("Here is the list of common friends of", uid1, "and", uid2)
common=net.getCommonFriends(uid1,uid2)
for item in common:
    print(item, end=" ")



    
