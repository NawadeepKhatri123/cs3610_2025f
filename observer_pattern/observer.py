from interfaces import Observer

class Follower(Observer):
    def __init__(self, username):
        self.username = username

    def update(self, message, owner_name):
        print(" ->", self.username, "got update from", owner_name, ":", message)

    def follow(self, channel):
        channel.attach(self)

    def unfollow(self, channel):
        channel.detach(self)
