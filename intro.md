# Faster Python

## Measuring Performance

### Benchmarking

* timeit

    * Command line interface

    ```bash
    $ python -m timeit '"-".join(str(n) for n in range(100))'
    10000 loops, best of 3: 40.3 usec per loop
    ```

    * In Python

    ```python
    import timeit
    >>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    0.8187260627746582
    ```

    * As IPython Magic Function
    
    ```python
    In [1]: %timeit "-".join(str(n) for n in range(100))
    10000 loops, best of 3: 25.4 µs per loop

    In [2]: %timeit "-".join(str(n) for n in xrange(100))
    10000 loops, best of 3: 24.1 µs per loop

    In [3]: %timeit "-".join([str(n) for n in xrange(100)])
    10000 loops, best of 3: 21.3 µs per loop

    In [4]: %timeit "-".join(map(str, [(n) for n in xrange(100)]))
    100000 loops, best of 3: 18.2 µs per loop

    In [5]: %timeit "-".join(map(str, ((n) for n in xrange(100))))
    10000 loops, best of 3: 20.9 µs per loop

    In [6]: %timeit "-".join(map(str, xrange(100)))
    100000 loops, best of 3: 13.1 µs per loop

    In [7]: %timeit "-".join(map(str, range(100)))
    100000 loops, best of 3: 13.5 µs per loop
    ```

### Profiling

#### Definition

> A profile is a set of statistics that describes how often and for how long various parts of the program executed.

#### cProfiler

* In Python

```python
import cProfile
cProfile.run('re.compile("foo|bar")')
```

```python
cProfile.run('re.compile("foo|bar")', 'restats')
```

```python
p = cProfile.Profile()
p.runcall(re.compile, "foo|bar")
p.print_stats()
```

* Command line interface

```bash
python -m cProfile -o restats test.py
```

#### pstats

```python
import pstats
p = pstats.Stats('restats')
p.strip_dirs().sort_stats('cumtime').print_stats(30)
```

#### RunSnakeRun

```bash
runsnake32 restats
```
