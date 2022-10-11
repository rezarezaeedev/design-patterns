class SingletonMetaclass(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Klass(metaclass=SingletonMetaclass):
    pass


k1=Klass()
k2=Klass()
k3=Klass()

print(id(k1))
print(id(k2))
print(id(k3))

        