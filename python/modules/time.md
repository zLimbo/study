```python
import time
dir(time)

['_STRUCT_T
 '__doc__',
 '__loader_
 '__name__'
 '__package
 '__spec__'
 'altzone',
 'asctime',
 'ctime',  
 'daylight'
 'get_clock
 'gmtime', 
 'localtime
 'mktime', 
 'monotonic
 'monotonic
 'perf_coun
 'perf_coun
 'process_t
 'process_t
 'sleep',  
 'strftime'
 'strptime'
 'struct_ti
 'thread_ti
 'thread_ti
 'time',   
 'time_ns',
 'timezone'
 'tzname'] 
```



#### `time.strftime`

```python
strftime(...)
    strftime(format[, tuple]) -> string

    Convert a time tuple to a string according to a format specification.
    See the library reference manual for formatting codes. When the time tuple
    is not present, current time as returned by localtime() is used.

    Commonly used format codes:

    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.

    Other codes may be available on your platform.  See documentation for
    the C library strftime function.
```



#### ` time.strptime`
```python
strptime(string, format) -> struct_time

    Parse a string to a time tuple according to a format specification.
    See the library reference manual for formatting codes (same as
    strftime()).

    Commonly used format codes:

    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.

    Other codes may be available on your platform.  See documentation for
    the C library strftime function.
```
#### `time.time` 和 `time.time_ns`

```python
time(...)
    time() -> floating point number

    Return the current time in seconds since the Epoch.
    Fractions of a second may be present if the system clock provides them.

time_ns(...)
    time_ns() -> int

    Return the current time in nanoseconds since the Epoch.
```
#### `time.sleep`

```python
sleep(...)
    sleep(seconds)

    Delay execution for a given number of seconds.  The argument may be
    a floating point number for subsecond precision.
```

#### `time.asctime`

```python
asctime(...)
    asctime([tuple]) -> string

    Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
    When the time tuple is not present, current time as returned by localtime()
    is used.

    
```

#### `time.ctime`

```python
ctime(...)
    ctime(seconds) -> string

    Convert a time in seconds since the Epoch to a string in local time.
    This is equivalent to asctime(localtime(seconds)). When the time tuple is
    not present, current time as returned by localtime() is used.
```

#### `time.gmtime`

```python
gmtime(...)
    gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                           tm_sec, tm_wday, tm_yday, tm_isdst)

    Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
    GMT).  When 'seconds' is not passed in, convert the current time instead.

    If the platform supports the tm_gmtoff and tm_zone, they are available as
    attributes only.
```

#### `time.mktime`

```python
mktime(...)
    mktime(tuple) -> floating point number

    Convert a time tuple in local time to seconds since the Epoch.
    Note that mktime(gmtime(0)) will not generally return zero for most
    time zones; instead the returned value will either be equal to that
    of the timezone or altzone attributes on the time module.
```

#### `time.localtime`

```python
localtime(...)
    localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                              tm_sec,tm_wday,tm_yday,tm_isdst)

    Convert seconds since the Epoch to a time tuple expressing local time.
    When 'seconds' is not passed in, convert the current time instead.
```

