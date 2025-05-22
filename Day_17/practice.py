# Class practice

class User:
    # Constructor for multiple custom attributes
    def __init__(self, user_id, user_name):
        # Everytime a new user is created, this print statement and all attributes will be triggered
        print("new user being created..")
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Custom object
user_1 = User("001", "Ahmed")
# Custom attributes
# user_1.id = "001"
# user_1.username = "Ahmed"
print (user_1.username)

user_2 = User("002", "Obama")
# user_1.id = "002"
# user_2.username = "Obama"
print (user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)