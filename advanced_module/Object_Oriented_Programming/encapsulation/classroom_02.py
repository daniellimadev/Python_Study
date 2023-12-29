# Relations between classes: association, aggregation and composition
# Association is a type of relationship where objects
# are linked within the system.
# This is the most common relationship between objects and has subsets
# such as aggregation and composition (which we will see later).
# Generally, we have an association when an object has
# an attribute that references another object.
# Binding does not specify how an object controls
# the life cycle of another object.
class Writer:
    def __init__(self, name) -> None:
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, tool):
        self._tool = tool


class WriteTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} is writing'


writer = Writer('Luiz')
pen = WriteTool('Bic Pen')
writing_machine = WriteTool('Machine')
writer.tool = writing_machine

print(pen.write())
print(writing_machine.write())
print(writer.tool.write())