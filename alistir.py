# # --------------------------------------------------
#
#
# class Shape:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def print_size(self):
#         print("{} by {}".format(self.width, self.length))
#
#
# class Square(Shape):
#     def calculate_area(self):
#         return self.width * self.length
#
#
# a_square = Square(20, 20)
# a_square.print_size()
# print(a_square.calculate_area())
#
#
# # --------------------------------------------------
#
#
# class Mammal:
#     def __init__(self, name):
#         self.hunger = 100
#         self.tired = 100
#         self.name = name
#
#     def print_result(self, amount, action):
#         print('{} {} decreased by {}'.format(self.name, action, amount))
#
#     def eat(self, decrease):
#         self.hunger -= decrease
#         self.print_result(decrease, 'hunger')
#
#     def sleep(self, decrease):
#         self.tired -= decrease
#         self.print_result(decrease, 'tiredness')
#
#
# class Dolphin(Mammal):
#     pass
#
#
# class Tiger(Mammal):
#     def sleep(self, decrease):
#         self.tired -= decrease
#         print('The tiger is tired!')
#
#
# dolp = Dolphin('Dolpy')
# dolp.eat(25)
# dolp.sleep(20)
# tig = Tiger('Tig')
# tig.eat(35)
# tig.sleep(10)
#
# # --------------------------------------------------


