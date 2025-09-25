from typing import List, Any

def binsok(a: List[Any], x: Any) -> int:
    #Returnerar index för x i a, eller -1 om x saknas
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid - 1
        else:
            return mid
    return -1

def main():
    indata = input().strip()
    the_list = indata.split()

    key = input().strip()
    while key != "#":
        idx = binsok(the_list, key)
        if idx == -1:
            print(None)
        else:
            print(the_list[idx])
        key = input().strip()

if __name__ == "__main__":
    main()