class Youtube:
    def __init__(self, username, subscribers=0, subscription= 0) -> None:
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription

    def subscribe(self, user):
        user.subscribers +=1
        self.subscription +=1 


user1 = Youtube('Vedant')
print(user1.username, user1.subscribers)

user2 = Youtube('Varnika', 100)
print(user2.username, user2.subscribers)