class Users:

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username


    def describe_user(self):
        print("User information: \n ")
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Username: " + self.username)

    def greet_user(self):
        print("Welcome " + self.username)

###child class

class Admins(Users):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.priveleges = Priveleges()

class Priveleges():

    def __init__(self, priveleges = []):
        priveleges = ['can add', 'can delete']
        self.priveleges = priveleges

    def show_priveleges(self):
        for each in self.priveleges:
            print(each)




#user = Admins("Harman", "Mahal", "jatt")
#user.describe_user()
#user.priveleges.show_priveleges()