from song import Song
import timeit
from bubblesort import bubblesort
from quicksort import quicksort

def create_unsorted_list(filename="unique_tracks.txt"):
    try:
        unsorted_songs = []
        print("Loading songs...")
        with open(filename, "r", encoding="utf-8") as file:
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

def benchmark_sorting(unsorted_songs, attribute: str):
    sizes = [1000, 10000, 100000, 1000000]

    print(f"\n{'n':<12}{'Bubblesort (s)':<25}{'Quicksort (s)':<25}")
    print("-" * 60)

    for n in sizes:
        sublist = unsorted_songs[:n]

        # Bubblesort: bara för små listor
        if n <= 10000:
            bubble_time = timeit.timeit(
                stmt=lambda: bubblesort(sublist, attribute),
                number=1
            )
            bubble_str = f"{bubble_time:.4f}"
        else:
            bubble_str = "för långsam"

        # Quicksort
        quick_time = timeit.timeit(
            stmt=lambda: quicksort(sublist, attribute),
            number=1
        )
        quick_str = f"{quick_time:.4f}"

        print(f"{n:<12}{bubble_str:<25}{quick_str:<25}")

def main():
    unsorted_songs = create_unsorted_list()
    attribute = "title"  # sortera på låttitlar

    benchmark_sorting(unsorted_songs, attribute)

if __name__ == "__main__":
    main()
