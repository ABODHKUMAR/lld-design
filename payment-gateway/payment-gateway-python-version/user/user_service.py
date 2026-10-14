import random

from user.user import User
from user.user_do import userDo

class UserService:

    users_list = []

    def add_user(self, user_do: userDo) -> userDo:

        user_obj = User()
        user_obj.setUserName(user_do.get_name())
        user_obj.setEmail(user_do.set_mail())
        user_do.se