
def median(data):
    return sorted(data)[len(data)//2]

def mode(data):
    from collections import Counter
    return Counter(data).most_common(1)[0][0]
