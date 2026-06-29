def add(a, b):
    return a + b


def _normalize(x):
    # TODO: figure out what normalization this was supposed to do
    return x


def process(items):
    out = []
    for it in items:
        out.append(_normalize(it))
    # XXX half-finished; original intent unclear
    return out
