class userDo:
    def __init__(self, user_id = None, name = None, mail = None):
        self.id = user_id
        self.name = name
        self.mail = mail

    def set_id(self, user_id):
        self.id = user_id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        return self.name

    def set_mail(self, mail):
        self.mail = mail

    def get_mail(self):
        return self.mail


    def __str__(self):
        return (
            f"UserDo [uId = {self.id},"
            f"name = {self.name}, email = {self.self.mail}]"
        )