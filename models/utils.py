# this contains objects that aren't 1st class
# (don't have their own collection in the db)

class Address(object):
    "A street address."
    def __init__(self, s = "", c = "asd", st = "", pc = ""):
        self.street = s
        self.city = c
        self.state = st
        self.postalCode = pc

    def __str__(self):
        return self.street + '\n' + self.city + ', ' + self.state + ' ' + self.postalCode

class Score(object):
    "Grade for a class."

    def __init__(self, course=None, grd = 0.0):
        self.for_course = course
        self.grade = grd

    def __str__(self):
        return '%s: %s'%(self.for_course, self.grade)

    def passed(self):
        return self.grade >= 2.0
