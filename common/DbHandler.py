# TODO: This class is just a prototype and it's just for testing puroses

from werkzeug.security import safe_str_cmp

from common.Link import Link
from common.User import User

links = [
    Link("www.stackoverflow.com", ["programming"]),
    Link("www.geeksforgeeks.com", ["programming", "learning"])
]
users = [
    User(1, 'user1', 'zanjan', links[0]),
    User(2, 'user2', 'berlin', links),
]

class DbHandler():
    @staticmethod
    def validateLogin(username, password):
        username_table = {u.username: u for u in users}
        user = username_table.get(username, None)
        
        returnMessage = ""
        if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            returnMessage = user
        else:
            returnMessage = None

        return returnMessage

    @staticmethod
    def addNewUser(username, password):
        # Check if user exists
        for user in users:
            if safe_str_cmp(user.username.encode('utf-8'), username.encode('utf-8')):
                return 1

        # If user doesn't exist, get Id for it and Signup
        maxId = 0
        for user in users:
            if user.id > maxId:
                maxId = user.id

        # Add new user
        users.append(User(maxId+1, username, password))

        return 0

    @staticmethod
    def getLinks(username):
        returnMessage = ""
        for user in users:
            if user.username == username:
                returnMessage = user.links

        return returnMessage