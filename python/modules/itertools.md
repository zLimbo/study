#### itertools.count

```python
class count(builtins.object)
 |  count(start=0, step=1)
 |
 |  Return a count object whose .__next__() method returns consecutive values.
 |
 |  Equivalent to:
 |      def count(firstval=0, step=1):
 |          x = firstval
 |          while 1:
 |              yield x
 |              x += step
```

