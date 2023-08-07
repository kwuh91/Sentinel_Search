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


if __name__ == '__main__':
    array = (numpy.random.uniform(-100000, 100000, size=1000000000))

    num = array[random.randint(0, len(array) - 1)]

    start_time = timer()
    SentinelSearch(array, num)
    end_time = timer() - start_time

    print(f"\n--- {end_time} seconds ---")
