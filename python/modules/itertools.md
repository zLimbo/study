#### itertools.accumulate

```python
def accumulate(iterable, func=operator.add, *, initial=None):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], initial=100) --> 100 101 103 106 110 115
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total
```

```python
>>> data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
>>> list(accumulate(data, operator.mul))     # running product
[3, 12, 72, 144, 144, 1296, 0, 0, 0, 0]
>>> list(accumulate(data, max))              # running maximum
[3, 4, 6, 6, 6, 9, 9, 9, 9, 9]

# Amortize a 5% loan of 1000 with 4 annual payments of 90
>>> cashflows = [1000, -90, -90, -90, -90]
>>> list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt))
[1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]

# Chaotic recurrence relation https://en.wikipedia.org/wiki/Logistic_map
>>> logistic_map = lambda x, _:  r * x * (1 - x)
>>> r = 3.8
>>> x0 = 0.4
>>> inputs = repeat(x0, 36)     # only the initial value is used
>>> [format(x, '.2f') for x in accumulate(inputs, logistic_map)]
['0.40', '0.91', '0.30', '0.81', '0.60', '0.92', '0.29', '0.79', '0.63',
 '0.88', '0.39', '0.90', '0.33', '0.84', '0.52', '0.95', '0.18', '0.57',
 '0.93', '0.25', '0.71', '0.79', '0.63', '0.88', '0.39', '0.91', '0.32',
 '0.83', '0.54', '0.95', '0.20', '0.60', '0.91', '0.30', '0.80', '0.60']
```



#### itertools.chanin

```python
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
```



#### itertools.combinations

```python
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
        
#
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
```



#### itertools.combinations_with_replacement

```python
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)
#
def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices) 
```

#### itertools.compress

```python
def compress(data, selectors):
    # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
    return (d for d, s in zip(data, selectors) if s)
```



#### itertools.count

```python
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
# 当对浮点数计数时，替换为乘法代码有时精度会更好，例如： 
(start + step * i for i in count()) 
```

#### itertools.cycle

```python
def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
              yield element
```



#### itertools.repeat

```python
class repeat(builtins.object)
 |  repeat(object [,times]) -> create an iterator which returns the object
 |  for the specified number of times.  If not specified, returns the object
 |  endlessly.
```



#### itertools.takewhile

```python
class takewhile(builtins.object)
 |  takewhile(predicate, iterable, /)
 |
 |  Return successive entries from an iterable as long as the predicate evaluates to true for each entry.
```

#### itertools.dropwhile

```python
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```



#### itertools.filterfalse

```python
def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x
```



#### itertools.groupby

```python
class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        self.id = object()
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey, self.id))
    def _grouper(self, tgtkey, id):
        while self.id is id and self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)
```



#### itertools.permutations

```python
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
```



#### itertools.product

```python
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
```



#### itertools.starmap

```python
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
```



#### itertools.zip_longest

```python
def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)
```



#### 扩展工具集

```python
pip install more-itertools
```

> ```python
> def take(n, iterable):
>     "Return first n items of the iterable as a list"
>     return list(islice(iterable, n))
> 
> def prepend(value, iterator):
>     "Prepend a single value in front of an iterator"
>     # prepend(1, [2, 3, 4]) -> 1 2 3 4
>     return chain([value], iterator)
> 
> def tabulate(function, start=0):
>     "Return function(0), function(1), ..."
>     return map(function, count(start))
> 
> def tail(n, iterable):
>     "Return an iterator over the last n items"
>     # tail(3, 'ABCDEFG') --> E F G
>     return iter(collections.deque(iterable, maxlen=n))
> 
> def consume(iterator, n=None):
>     "Advance the iterator n-steps ahead. If n is None, consume entirely."
>     # Use functions that consume iterators at C speed.
>     if n is None:
>         # feed the entire iterator into a zero-length deque
>         collections.deque(iterator, maxlen=0)
>     else:
>         # advance to the empty slice starting at position n
>         next(islice(iterator, n, n), None)
> 
> def nth(iterable, n, default=None):
>     "Returns the nth item or a default value"
>     return next(islice(iterable, n, None), default)
> 
> def all_equal(iterable):
>     "Returns True if all the elements are equal to each other"
>     g = groupby(iterable)
>     return next(g, True) and not next(g, False)
> 
> def quantify(iterable, pred=bool):
>     "Count how many times the predicate is true"
>     return sum(map(pred, iterable))
> 
> def padnone(iterable):
>     """Returns the sequence elements and then returns None indefinitely.
> 
>     Useful for emulating the behavior of the built-in map() function.
>     """
>     return chain(iterable, repeat(None))
> 
> def ncycles(iterable, n):
>     "Returns the sequence elements n times"
>     return chain.from_iterable(repeat(tuple(iterable), n))
> 
> def dotproduct(vec1, vec2):
>     return sum(map(operator.mul, vec1, vec2))
> 
> def flatten(list_of_lists):
>     "Flatten one level of nesting"
>     return chain.from_iterable(list_of_lists)
> 
> def repeatfunc(func, times=None, *args):
>     """Repeat calls to func with specified arguments.
> 
>     Example:  repeatfunc(random.random)
>     """
>     if times is None:
>         return starmap(func, repeat(args))
>     return starmap(func, repeat(args, times))
> 
> def pairwise(iterable):
>     "s -> (s0,s1), (s1,s2), (s2, s3), ..."
>     a, b = tee(iterable)
>     next(b, None)
>     return zip(a, b)
> 
> def grouper(iterable, n, fillvalue=None):
>     "Collect data into fixed-length chunks or blocks"
>     # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
>     args = [iter(iterable)] * n
>     return zip_longest(*args, fillvalue=fillvalue)
> 
> def roundrobin(*iterables):
>     "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
>     # Recipe credited to George Sakkis
>     num_active = len(iterables)
>     nexts = cycle(iter(it).__next__ for it in iterables)
>     while num_active:
>         try:
>             for next in nexts:
>                 yield next()
>         except StopIteration:
>             # Remove the iterator we just exhausted from the cycle.
>             num_active -= 1
>             nexts = cycle(islice(nexts, num_active))
> 
> def partition(pred, iterable):
>     'Use a predicate to partition entries into false entries and true entries'
>     # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
>     t1, t2 = tee(iterable)
>     return filterfalse(pred, t1), filter(pred, t2)
> 
> def powerset(iterable):
>     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
>     s = list(iterable)
>     return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
> 
> def unique_everseen(iterable, key=None):
>     "List unique elements, preserving order. Remember all elements ever seen."
>     # unique_everseen('AAAABBBCCDAABBB') --> A B C D
>     # unique_everseen('ABBCcAD', str.lower) --> A B C D
>     seen = set()
>     seen_add = seen.add
>     if key is None:
>         for element in filterfalse(seen.__contains__, iterable):
>             seen_add(element)
>             yield element
>     else:
>         for element in iterable:
>             k = key(element)
>             if k not in seen:
>                 seen_add(k)
>                 yield element
> 
> def unique_justseen(iterable, key=None):
>     "List unique elements, preserving order. Remember only the element just seen."
>     # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
>     # unique_justseen('ABBCcAD', str.lower) --> A B C A D
>     return map(next, map(operator.itemgetter(1), groupby(iterable, key)))
> 
> def iter_except(func, exception, first=None):
>     """ Call a function repeatedly until an exception is raised.
> 
>     Converts a call-until-exception interface to an iterator interface.
>     Like builtins.iter(func, sentinel) but uses an exception instead
>     of a sentinel to end the loop.
> 
>     Examples:
>         iter_except(functools.partial(heappop, h), IndexError)   # priority queue iterator
>         iter_except(d.popitem, KeyError)                         # non-blocking dict iterator
>         iter_except(d.popleft, IndexError)                       # non-blocking deque iterator
>         iter_except(q.get_nowait, Queue.Empty)                   # loop over a producer Queue
>         iter_except(s.pop, KeyError)                             # non-blocking set iterator
> 
>     """
>     try:
>         if first is not None:
>             yield first()            # For database APIs needing an initial cast to db.first()
>         while True:
>             yield func()
>     except exception:
>         pass
> 
> def first_true(iterable, default=False, pred=None):
>     """Returns the first true value in the iterable.
> 
>     If no true value is found, returns *default*
> 
>     If *pred* is not None, returns the first item
>     for which pred(item) is true.
> 
>     """
>     # first_true([a,b,c], x) --> a or b or c or x
>     # first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
>     return next(filter(pred, iterable), default)
> 
> def random_product(*args, repeat=1):
>     "Random selection from itertools.product(*args, **kwds)"
>     pools = [tuple(pool) for pool in args] * repeat
>     return tuple(random.choice(pool) for pool in pools)
> 
> def random_permutation(iterable, r=None):
>     "Random selection from itertools.permutations(iterable, r)"
>     pool = tuple(iterable)
>     r = len(pool) if r is None else r
>     return tuple(random.sample(pool, r))
> 
> def random_combination(iterable, r):
>     "Random selection from itertools.combinations(iterable, r)"
>     pool = tuple(iterable)
>     n = len(pool)
>     indices = sorted(random.sample(range(n), r))
>     return tuple(pool[i] for i in indices)
> 
> def random_combination_with_replacement(iterable, r):
>     "Random selection from itertools.combinations_with_replacement(iterable, r)"
>     pool = tuple(iterable)
>     n = len(pool)
>     indices = sorted(random.randrange(n) for i in range(r))
>     return tuple(pool[i] for i in indices)
> 
> def nth_combination(iterable, r, index):
>     'Equivalent to list(combinations(iterable, r))[index]'
>     pool = tuple(iterable)
>     n = len(pool)
>     if r < 0 or r > n:
>         raise ValueError
>     c = 1
>     k = min(r, n-r)
>     for i in range(1, k+1):
>         c = c * (n - k + i) // i
>     if index < 0:
>         index += c
>     if index < 0 or index >= c:
>         raise IndexError
>     result = []
>     while r:
>         c, n, r = c*r//n, n-1, r-1
>         while index >= c:
>             index -= c
>             c, n = c*(n-r)//n, n-1
>         result.append(pool[-1-n])
>     return tuple(result)
> ```
>
> 