# Faster Python

## Measuring Performance

### Benchmarking

* timeit

    * Command line interface

    ```bash
    python -m timeit '"-".join(str(n) for n in range(100))'
    ```

### Profiling

#### Definition

> A profile is a set of statistics that describes how often and for how long various parts of the program executed.

#### cProfiler

* Run in Python

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
