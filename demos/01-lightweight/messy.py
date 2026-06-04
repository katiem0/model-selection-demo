def sum_evens(values):
    total = 0
    for value in values:
        if value % 2 == 0:
            total += value
    return total


def group_by_first_letter(words):
    d = {}
    for w in words:
        k = w[0].lower()
        if k not in d:
            d[k] = []
        d[k].append(w)
    return d


def top_n(scores, n):
    return sorted(scores, reverse=True)[:n]


def safe_divide(a,b):
    if b == 0:
        return None
    return a / b


def merge_counts(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return out


def first_match(items, pred):
    for it in items:
        if pred(it):
            return it
    return None
