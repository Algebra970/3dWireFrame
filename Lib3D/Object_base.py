from MathLib import MathLib as ML

class Object_base():
    def __init__(self, obj=None, filename=None):
        return

    def loadJson(self, filename):
        return self

    def scale(self, scale, state=False, elements=[]):
        return self

    def rotate(self, x, y, z, dcm, state=False, elements=[]):
        return self

    def translate(self, x, y, z, V, state=False, elements=[]):
        return self

    def getShape(self):
        return []

    def getLines(self):
        return []

class Object_container(Object_base):
    def __init__(self, objList=[], connections=[]):
        self.shapes = objList
        self.connections = connections

    def reset(self):
        for shape in self.shapes:
            shape.reset()
        return self

    def scale(self, scale, initShape=False, elements=[]):
        if elements == []:
            for shape in self.shapes:
                shape.scale(scale, initShape)
        else:
            for elm in elements:
                self.shapes[elm].rotate(x, y, z, dcm, initShape)                
        return self

    def rotate(self, x=0, y=0, z=0, dcm=None, initShape=False, elements=[]):
        if elements == []:
            for shape in self.shapes:
                shape.rotate(x, y, z, dcm, initShape)
        else:
            for elm in elements:
                self.shapes[elm].rotate(x, y, z, dcm, initShape)                
        return self

    def translate(self, x=0, y=0, z=0, V=None, initShape=False, elements=[]):
        if elements == []:
            for shape in self.shapes:
                shape.translate(x, y, z, V, initShape)
        else:
            for elm in elements:
                self.shapes[elm].translate(x, y, z, dcm, initShape)                
        return self

    def getShape(self):
        shapes = []
        for shape in self.shapes:
            shapes += shape.getShape()
        return shapes

    def getLines(self):
        lines = []
        for shape in self.shapes:
            lines += shape.getLines()

        for line in self.connections:
            p0, p1 = line
            shapes0 = self.shapes[p0[0]].getShape()
            shapes1 = self.shapes[p1[0]].getShape()
            lines += [(shapes0[p0[1]], shapes1[p1[1]])]
        return lines

    
