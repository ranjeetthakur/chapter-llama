class rank_zero_only:
    rank = 0
    def __init__(self, fn=None):
        self.fn = fn
    def __call__(self, *args, **kwargs):
        if self.fn:
            return self.fn(*args, **kwargs)
    def __get__(self, obj, objtype=None):
        return self

def rank_prefixed_message(message):
    return message
