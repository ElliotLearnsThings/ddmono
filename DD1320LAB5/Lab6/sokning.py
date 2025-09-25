from song import Song 
from linsok import linsok
from binsok import binsok
from hashtab import hashtab
import timeit

def create_unsorted_list():
    try:
        unsorted_songs = []
        print("Loading songs...")
        with open("unique_tracks.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("<SEP>")
                if len(parts) == 4:
                    trackid, songid, artistname, title = parts
                    unsorted_songs.append(Song(trackid, songid, artistname, title))
        print("Songs loaded:", len(unsorted_songs))
        return unsorted_songs
    except Exception as e:
        print("Error:", e)
        return []

def create_sorted_list(unsorted_songs, attribute: str):
    """Return songs sorted by the given attribute name."""
    return sorted(unsorted_songs, key=lambda s: getattr(s, attribute))


def linear_search_example(unsorted_songs, attribute):
    search = input(f"Enter {attribute} to search: ").strip()

    index = linsok(unsorted_songs, attribute, search)
    if index != -1:
        print("Found:", unsorted_songs[index], "at index", index)
    else:
        print("Not found")


def binary_search_example(sorted_songs, attribute: str):
    search = input(f"Enter {attribute} to search: ").strip()

    # Extrahera attributvärden för binärsökning
    values = [getattr(s, attribute) for s in sorted_songs]

    index = binsok(values, search)
    if index != -1:
        print("Found:", sorted_songs[index], "at index", index)
    else:
        print("Not found")

def hashtable_search_example(hashtable, attribute: str):
    search = input(f"Enter {attribute} to search (hashtable): ").strip()

    if search in hashtable:
        print("Found (hashtable):", hashtable[search])
    else:
        print("Not found (hashtable)")

def main():
    unsorted_songs = create_unsorted_list()
    attribute = "title"

    sorted_songs = create_sorted_list(unsorted_songs, attribute) #sorterar
    hashtable = hashtab(unsorted_songs, attribute)

    n = len(unsorted_songs)
    print("Antal element =", n)

    # väljer ett element att söka efter
    test_key = getattr(unsorted_songs[-1], attribute)
    print(f"Testkey ({attribute}) =", test_key)

    # extraherar attributvärden för binärsökning
    values = [getattr(s, attribute) for s in sorted_songs]


    for n in [250000, 500000, 1000000]:
        print(f"\n--- n = {n} ---")

        # gör en mindre lista
        sub_unsorted = unsorted_songs[:n]
        sub_sorted = create_sorted_list(sub_unsorted, attribute)
        sub_hashtable = hashtab(sub_unsorted, attribute)

        # välj testnyckel (sista elementet i sublistan)
        test_key = getattr(sub_unsorted[-1], attribute)
        print(f"Testkey ({attribute}) =", test_key)

        # extrahera attributvärden för binärsökning
        values = [getattr(s, attribute) for s in sub_sorted]

        # linjärsökning tidtagning
        linjtid = timeit.timeit(
            stmt=lambda: linsok(sub_unsorted, attribute, test_key),
            number=100
        ) / 100
        print("Linjärsökning:", round(linjtid, 8), "sekunder per sökning")

        # binärsökning tidtagning
        bintid = timeit.timeit(
            stmt=lambda: binsok(values, test_key),
            number=10000
        ) / 10000
        print("Binärsökning:", round(bintid, 8), "sekunder per sökning")

        # hashtabell sökning tidtagning
        hashtid = timeit.timeit(
            stmt=lambda: sub_hashtable.get(test_key, None),
            number=100000
        ) / 100000
        print("Hashtabellsökning:", round(hashtid, 8), "sekunder per sökning")


if __name__ == "__main__":
    main()