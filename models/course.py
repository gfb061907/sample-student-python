import models.modelbase as modelbase

class Course(modelbase.ModelBase):
    "A named course"

    collectionName = 'courses'

    def __init__(self, name='name not set'):
        self.name = name

    def __str__(self):
        return 'Course ' + self.name

