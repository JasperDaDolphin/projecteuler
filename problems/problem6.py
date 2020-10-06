def problem():
    _range = range(0, 101)
    return sum(x for x in _range)**2 - sum(x**2 for x in _range) 