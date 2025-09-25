def linsok(list, attribute, search):
    for i in range(len(list)):
        if getattr(list[i], attribute) == search:
            return i
    return -1



def main():
    indata = input().strip()
    the_list = indata.split()

    key = input().strip()
    while key != "#":
        idx = linsok(the_list, key)
        if idx == -1:
            print(None)
        else:
            print(the_list[idx])
        key = input().strip()

if __name__ == "__main__":
    main()  