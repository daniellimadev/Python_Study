# @property + @setter - getter and setter in Python mode
# - as getter
# - to avoid breaking client code
# - to enable setter
# - to perform actions when obtaining an attribute
# Attributes that start with one or two underscores
# should not be used outside the class.
# 🐍🤓🤯🤯🤯🤯
class Pen:
    def __init__(self, color):
        # private protected
        self.color = color
        self._color_cap = None

    @property
    def color(self):
        print("I'M IN GETTER")
        return self._color

    @color.setter
    def color(self, value):
        print("I'M IN THE SETTER")
        self._color = value

    @property
    def color_cap(self):
        return self._color_cap

    @color_cap.setter
    def ccolor_cap(self, value):
        self._cor_cap = value


pen = Pen('Blue')
pen.color = 'Pink'
pen.cor_cap = 'Blue'
print(pen.color)
print(pen.color_cap)