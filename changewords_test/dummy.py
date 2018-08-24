

def something(helloworld, *args, **kwargs):
    initial = helloworld
    return initial + 1


class Awesome(object):
    """docstring for Awesome."""

    def __init__(self, field):
        super(Awesome, self).__init__()
        self.field = field
