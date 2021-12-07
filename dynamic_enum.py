class DynamicEnum(Enum):
    def __init__(self, *args):
        for arg in args:
            setattr(self, arg, arg)
    def __new__(cls, *args, **kwargs):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj.__value__ = value
        return obj
