import random

def quicksort(songs, attribute: str):
    if len(songs) <= 1:
        return songs
    pivot = getattr(random.choice(songs), attribute)  # slumpa pivot
    less = [s for s in songs if getattr(s, attribute) < pivot]
    equal = [s for s in songs if getattr(s, attribute) == pivot]
    greater = [s for s in songs if getattr(s, attribute) > pivot]
    return quicksort(less, attribute) + equal + quicksort(greater, attribute)
