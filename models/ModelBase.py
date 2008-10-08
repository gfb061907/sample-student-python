from _10gen import db, ObjectId

class ModelMeta(type):
    def __new__(mcls, name, bases, attrs):
        cls = super(ModelMeta, mcls).__new__(mcls, name, bases, attrs)
        if attrs.get('__metaclass__', None) == mcls:
            # Don't intercept creation with __metaclass__ = ModelMeta
            # Only intercept creation of subclasses of
            # classes with __metaclass__ = ModelMeta
            return cls


        cls._c = db[cls.collectionName]
        cls._c.setConstructor(cls)
        return cls

    def find(cls, key=None, fields=None):
        return cls._c.find(key, fields)

    def findOne(cls, key="", create=False):
        if key == "" or key == None:
            if create:
                return cls()
            return None
        if isinstance(key, str):
            key = ObjectId(key)

        o = cls._c.findOne(key);
        if create and o == None:
            o = cls()
        return o

class ModelBase(object):
    __metaclass__ = ModelMeta
    def save(self):
        return self._c.save(self)

    def remove(self, key=None):
        if key == None:
            key = {}
            if not hasattr(self, '_id'):
                return
            key['_id'] = self._id
        return self._c.remove(key)
