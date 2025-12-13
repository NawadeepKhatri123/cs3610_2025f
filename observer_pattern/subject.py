from interfaces import Subject, Observer

class ChannelOwner(Subject):
    def __init__(self, name):
        self.name = name
        self.followers = []
        self.last_msg = None

    def attach(self, observer):
        if observer not in self.followers:
            self.followers.append(observer)
            print(observer.username, "followed", self.name)

    def detach(self, observer):
        if observer in self.followers:
            self.followers.remove(observer)
            print(observer.username, "unfollowed", self.name)

    def notify(self):
        print("notifying followers...")
        for f in self.followers:
            f.update(self.last_msg, self.name)

    def post_message(self, msg):
        print("\n", self.name, "posted:", msg)
        self.last_msg = msg
        self.notify()

    def remove_follower(self, obs):
        print(self.name, "removed", obs.username)
        self.detach(obs)
