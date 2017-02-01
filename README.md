# Wrapped Types
Author: Darren Struthers -  <dstruthers@gmail.com>

Wrapped types provide behavior that is similar to class inheritance, albeit with
some key deviations. Most notably, wrapped types coerce values returned by
inherited methods to the current (descendent) class type instead of leaving them
in their native, inherited, type.

The following example illustrates this distinction:

```python
>>> from wrapped_types import wrapped
>>> class MyStr(str): pass # inherit from str directly
...
>>> class MyStr2(wrapped(str)): pass # wrap str instead
...
>>> foo = MyStr('foo')
>>> foo.upper()
'FOO'
>>> type(foo.upper())
<type 'str'>
>>> bar = MyStr2('bar')
>>> bar.upper()
'BAR'
>>> type(bar.upper())
<class '__main__.MyStr2'>
```

Another important distinction is that wrapped types are not class descendents of
the types they wrap.

```python
>>> isinstance(foo, str)
True
>>> isinstance(bar, str)
False
```

## What's the Point?

Continuing from the above example, consider situations like this:

```python
>>> type(foo)
<class '__main__.MyStr'>
>>>foo += 'baz'
>>> type(foo)
<type 'str'>
```
The fallback to the base class might be harmless in some cases, but problematic
in others. It's not difficult to imagine the inherited class containing
additional data that would be lost in this situation.

A single programmer can obviously account for, and work around, this situation,
but if a programmer is writing a class for a library or for others to use, it
may be advantageous to provide some protections in certain situations. A wrapped
type may be able to provide that protection.

```python
>>> type(bar)
<class '__main__.MyStr2'>
>>> bar += 'baz'
>>> type(bar)
<class '__main__.MyStr2'>
```

## How Type Conversion Works

Results of method calls are only converted for types which support equality
testing via the `==` operator. Essentially, a wrapper around the method calls
compares the method's response to a copy of the response that is explicitly
converted to the current object's class. If the two values are deemed equal,
the instance of the current class is returned instead of the original return
value.

For this reason, wrapped types may be unsuitable for classes whose methods
produce side effects in addition to merely returning a value.

If performance is paramount, or when a class's constructor has a lengthy
execution time for some reason, the additional cost of this wrapping and
inspection may be another deterrent.

## Your Mileage May Vary

I authored this library for my own use, and have found certain applications for
it in my own programming. If you happen to try it out, any feedback is
appreciated.
