class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD BEFORE Parent altered()")
        super(Child, self).altered()
        print("CHILD AFTER Parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
