import time
import day6 as d


if __name__ == '__main__':
    start = time.perf_counter()

    d.solve()

    elapsed_time = (time.perf_counter() - start) * 1000
    print("Execution time (ms):", elapsed_time)
