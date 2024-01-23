# class Robot():
#     battery_level = 12
#     degrees_of_freedom = 25


# robot_a = Robot()
# robot_b = Robot()
# print(robot_a.battery_level) 


class StarCookie:
    milk = 0.1
    def __init__(self, color, weight) -> None:
        self.color = color
        self.weight = weight


star_cookie1 = StarCookie("Red", 22)
print(star_cookie1.color, star_cookie1.weight)
star_cookie2 = StarCookie("Blue", 15)
print(star_cookie1.color, star_cookie1.weight, star_cookie1.milk)



class Youtube:
    def __init__(self, username, subscribers=0) -> None:
        self.username = username
        self.subscribers = subscribers


user1 = Youtube('Vedant')
print(user1.username, user1.subscribers)

user2 = Youtube('Varnika', 100)
print(user2.username, user2.subscribers)