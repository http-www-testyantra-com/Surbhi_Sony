class NameException(Exception):
    def __int__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return "exception ois because of " + str(self.msg)

raise NameException("hello world")

