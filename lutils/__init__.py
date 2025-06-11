def openf(path, *args, **kwargs):
    return open(path, *args, **kwargs)

def writef(path, data, mode='w'):
    with open(path, mode) as f:
        if isinstance(data, (list, tuple)):
            f.write('\n'.join(str(x) for x in data))
        else:
            f.write(str(data))
