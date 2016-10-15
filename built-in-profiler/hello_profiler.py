import time
import cProfile


def some_func():
    i = 0
    while i < 1000000:
        i += 1
    time.sleep(0.5)


def main():
    p = cProfile.Profile()
    p.runcall(some_func)
    p.print_stats()

if __name__ == "__main__":
    main()
