class NameException(Exception):
    def __int__(self, msg = None):
        self.msg = msg


try:
    raise NameException("hello world")
except NameException as e:
    print(e)
