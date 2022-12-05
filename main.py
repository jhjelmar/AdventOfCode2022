import time
import day5

if __name__ == '__main__':
    start = time.perf_counter()

    day5.part1()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)
