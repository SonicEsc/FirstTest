class Parent():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def do_parent_stuff(self):
        print(self.a, self.b)

class Child(Parent):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d
    def do_child_stuff(self):
        print(self.a, self.b, self.c, self.d)

p = Parent(3, 5)
p.do_parent_stuff()
c = Child(7, 9, 11, 13)
c.do_child_stuff()

#https://www.reddit.com/r/learnpython/comments/r5b7jo/can_anyone_here_explain_self_super_and_init_in/