import haversine from haversine
import hashlib


# format
class mgo:

    def __init__(self):
        self.Users = {}
        self.table = {}
        self.token = "21234589jkjidjfoai"
        self.messages = {}
        self.msgid = 0

    def user_exists(self,user,password):
        """Change logic to get info from db or firebase"""
        if user in self.Users:
            return True       ## Raise Exception
        else:
            return False

    def update_user(self,username,password):
        """Update username and password to db<Update this to communicate with firebase>"""
        self.Users[username] = password
        return token

    def add_user(self,username,password):
        """Add new usser to db"""

        if user_exists(username)
            pass   # later pass message user exists
        else:
            token = update_user(username,password)
            return token

    def login(self,username,password):
        """Logs user in the system <Needs to get data from firebase>"""
        if username in self.Users[username]:                  ##Update logic
            if password == self.Users[username]:
                return self.token
        if res is None:
            return None  # login failed

    def add_message(self,username,message,location):
        """Add a new message to the messages dictionary"""
        #### USE pandas or sql lite db to or get from firebase
        id = self.msgid + 1
        self.messages[id] = {"username":username,"message" : message ,"loc":location}
        self.push_to_users(id,location)

    def get_messages(location):
        """Returns all messages in given latitude and longitude range"""
        get_valid_msg_ids = get_msg_ids(location)
        res = [self.messages[id] for id in get_valid_msg_ids]
        return res

    def get_msg_ids(location):
        """Get all messges in the location range""" ###### Not needed
        ids = []
        for id in self.messages:
            if is_range(location,self.messages[id][location],radius):
                ids.append(ids)
        return ids

    def is_range(location1,location2),radius):
        """Checks if corodinates are in is_range
            Formula for Haversine Distance Algorithm between two places
            R = earth’s radius (mean radius = 6,371km)
            Δlat = lat2− lat1
            Δlong = long2− long1
            a = sin²(Δlat/2) + cos(lat1).cos(lat2).sin²(Δlong/2)
            c = 2.atan2(√a, √(1−a))
            d = R.c
        """
        distance = haversine(coord1, coord2) * 1000
        if distance <= radius:
            return True
        else:
            return False
