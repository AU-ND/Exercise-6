from dependant357891112 import *
from dep2ndant357891122 import *

print("ADMIN\n")
admin1 = Admin('bruhman', 'bean', 'BB', 'brown', 'Beanular', 0, 2)

admin1.describe2()
admin1.priviledges.privy()

admin2 = Admin('bruhlad', 'bean', 'BRB', 'red', 'Boneular', 0, 3)

admin2.describe2()
admin2.priviledges.privy()

admin1.describe2()
admin1.priviledges.privy()
admin1.priviledges.escalate()
admin1.priviledges.privy()

print(f"\nUSERS\n")
nd = User('n', 'd', 'nd', 'blurple', 'burger')
zh = User('z', 'h', 'zh', 'yelo', 'shenmue')
ne = User('n', 'e', 'ne', 'red', 'margar')

nd.describe()
zh.describe()
ne.describe()

nd.greet_user()
zh.greet_user()
ne.greet_user()

nd.login()
nd.login()
nd.loginreset()
nd.describe()