from collections import namedtuple

Task = namedtuple('Task',['summary','owner','done','id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    """Using no parameters should invoke defaults"""