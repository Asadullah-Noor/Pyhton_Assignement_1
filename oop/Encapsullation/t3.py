class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   # private password

    def check_password(self, pw):
        return self.__password == pw

    def change_password(self, old, new):

        # check old password
        if old != self.__password:
            print("Old password is incorrect")
            return

        # check length
        if len(new) < 8:
            print("Password must be at least 8 characters")
            return

        # check for number
        has_number = False
        for char in new:
            if char.isdigit():
                has_number = True
                break

        if not has_number:
            print("Password must contain at least 1 number")
            return

        # change password
        self.__password = new
        print("Password changed successfully")


# ---------------- Example ----------------
user = User("Asadullah12", "asadullahNor1")

print(user.check_password("asadullahNor1"))  # True

user.change_password("asadullahNor1", "newpass1")  # valid
user.change_password("wrong", "newpass2")          # old password incorrect
user.change_password("newpass1", "short")          # too short
user.change_password("newpass1", "password")       # no number