### contextlib



#### contextmanager

```python
contextmanager(func)
    @contextmanager decorator.

    Typical usage:

        @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        with some_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
```



#### closing

```python
class closing(AbstractContextManager)
 |  closing(thing)
 |
 |  Context to automatically close something at the end of a block.
 |
 |  Code like this:
 |
 |      with closing(<module>.open(<arguments>)) as f:
 |          <block>
 |
 |  is equivalent to this:
 |
 |      f = <module>.open(<arguments>)
 |      try:
 |          <block>
 |      finally:
 |          f.close()

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
```



#### suppress

```python
class suppress(AbstractContextManager)
 |  suppress(*exceptions)
 |
 |  Context manager to suppress specified exceptions
 |
 |  After the exception is suppressed, execution proceeds with the next
 |  statement following the with statement.
 |
 |       with suppress(FileNotFoundError):
 |           os.remove(somefile)
 |       # Execution still resumes here if the file was already removed
```



#### ExitStack

```python
class ExitStack(_BaseExitStack, AbstractContextManager)
 |  Context manager for dynamic management of a stack of exit callbacks.
 |
 |  For example:
 |      with ExitStack() as stack:
 |          files = [stack.enter_context(open(fname)) for fname in filenames]
 |          # All opened files will automatically be closed at the end of
 |          # the with statement, even if attempts to open files later
 |          # in the list raise an exception.
```

