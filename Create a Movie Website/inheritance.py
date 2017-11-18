class Parent():
    def __init__(self, last_name, eye_color):
        print('Parent __init__')
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print('Child __init__')
        Parent.__init__(self, last_name, eye_color)
        self.toys = toys

billy_cyrus = Parent('Cyrus', 'blue')
print(billy_cyrus.last_name)
miley_cyrus = Child('Cyrus', 'blue', 3)
print(miley_cyrus.toys)
