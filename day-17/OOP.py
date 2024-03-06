class dhairya:
    def __init__(self,user_id,user_name) :
        self.id = user_id
        self.name = user_name
        self.follower = 0
        self.following = 0
    def follow(self,user):
        user.follower += 1
        self.following += 1    


Dhairya = dhairya("1236","DhAiRyA") #object of this class 
Dhairya.username = "joshi"
Dhairya.id = "1236"
print(Dhairya.username)
print(Dhairya.id)


