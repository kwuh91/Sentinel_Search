import numpy
from numpy import random
from timeit import default_timer as timer


def SentinelSearch(arr: [float], key: float, n=None) -> None:
    if n is None: n = len(arr)

    last: float = arr[n - 1]
    arr[n - 1] = key

    i: int = 0
    while arr[i] != key:
        i += 1

    arr[n - 1] = last

    if i < n - 1 or arr[n - 1] == key:
        print(f"{key} is located at {i}\n(checking arr[{i}] = {arr[i]})")
    else:
        print(f"There is no {key} in an array")


def LinearSearch(arr: [float], key: float, n=None) -> None:
    if n is None: n = len(arr)
    flag: bool = True
    for i in range(n):
        if arr[i] == key:
            print(f"{key} is located at {i}\n(checking arr[{i}] = {arr[i]})")
            flag = False
            break
    if flag: print(f"There is no {key} in an array")


if __name__ == '__main__':
    print(f"TEST FOR {100000000} ELEMENTS")
    array = (numpy.random.uniform(-100000, 100000, size=100000000))

    num = array[random.randint(0, len(array) - 1)]

    print(f"\n---------Sentinel search---------")
    start_time = timer()
    SentinelSearch(array, num)
    end_time = timer() - start_time
    print(f"\n--- {end_time} seconds ---")

    print(f"\n\n---------Linear search---------")
    start_time2 = timer()
    LinearSearch(array, num)
    end_time2 = timer() - start_time
    print(f"\n--- {end_time2} seconds ---")
