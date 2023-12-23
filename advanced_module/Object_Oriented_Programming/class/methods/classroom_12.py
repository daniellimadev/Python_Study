# @property - a getter in Pythonic mode
# getter - a method to get an attribute
# color -> get_color()
# pythonic way - Python's way of doing things
# @property is a property of the object, it
# is a method that behaves like a
# attribute 🤯 🤯 🤯
# It is generally used in the following situations:
# - as getter
# - to avoid breaking client code
# - to enable setter
# - to perform actions when obtaining an attribute
# Client code - is the code that uses your code
class Pen:
    def __init__(self, color):
        self.tint_color = color

    @property
    def color(self):
        print('PROPERTY')
        return self.tint_color

    @property
    def color_cap(self):
        return 123456

##########################


pen = Pen('Blue')
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color)
print(pen.color_cap)

###################################

# class Pen:
# def __init__(self, color):
# self.paint_color = color

# def get_color(self):
# print('GET COLOR')
# return self.tint_color

# ##########################


# pen = Pen('Blue')
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())
# print(pen.get_color())