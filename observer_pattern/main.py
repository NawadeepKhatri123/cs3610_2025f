from subject import ChannelOwner
from observer import Follower

owner = ChannelOwner("Dr. Hanna")

a = Follower("Student_A")
b = Follower("Student_B")
c = Follower("Student_C")

a.follow(owner)
b.follow(owner)
c.follow(owner)

owner.post_message("Midterm grades are out")

b.unfollow(owner)

owner.post_message("Final exams just ended !!!!")

owner.remove_follower(c)

owner.post_message("!!! Happy Holidays !!!")
