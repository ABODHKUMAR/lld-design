class User:

    def __init__(self, user_id = None, user_name = None, email = None):
        self.userID = user_id
        self.userName = user_name
        self.email = email

    def getUserId(self):
        return self.userID
    
    def setUser(self, user_id):
        self.userID = user_id

    def getUserName(self):
        return self.userName

    def setUserName(self, user_name):
        self.userName = user_name
    
    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email


    def __str__(self):
        return (
            f"User [userId = {self.userID}], "
            f"name={self.userName}, email={self.email}]"
        )

    

