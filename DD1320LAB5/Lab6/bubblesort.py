def bubblesort(songs, attribute: str):
    n = len(songs)
    songs_copy = songs[:]  # kopia
    for i in range(n):
        for j in range(0, n - i - 1):
            if getattr(songs_copy[j], attribute) > getattr(songs_copy[j + 1], attribute):
                songs_copy[j], songs_copy[j + 1] = songs_copy[j + 1], songs_copy[j]
    return songs_copy
