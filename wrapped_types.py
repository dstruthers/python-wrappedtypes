class WrapperFactory(object):
    def __init__(self):
        self.types = {}

    def __call__(self, type_):
        try:
            return self.types[type_]
        except KeyError:
            try:
                self.types[type_] = self.wrap(type_)
                return self.types[type_]
            except NameError:
                raise

    def __getattr__(self, attr):
        try:
            return self.types[attr]
        except KeyError:
            try:
                self.types[attr] = self.wrap(eval(attr))
                return self.types[attr]
            except NameError:
                raise

    @staticmethod
    def wrap(type_):
        class Wrapped(object):
            def __init__(self, *args, **kwargs):
                self._value = type_(*args, **kwargs)

            def _convert(self, value):
                if type(value) == type_:
                    try:
                        mimic = self.__class__(value)
                        if mimic == value:
                            return mimic
                    except: pass
                return value

            if hasattr(type_, '__abs__'):
                def __abs__(self):
                    return self._convert(abs(self._value))

            if hasattr(type_, '__add__'):
                def __add__(self, other):
                    return self._convert(self._value + other)

            if hasattr(type_, '__and__'):
                def __and__(self, other):
                    return self._convert(self._value & other)

            if hasattr(type_, '__coerce__'):
                def __coerce__(self, other):
                    return (self._value, type_(other))

            if hasattr(type_, '__cmp__'):
                def __cmp__(self, other):
                    return cmp(self._value, other)

            if hasattr(type_, '__complex__'):
                def __complex__(self):
                    return complex(self._value)

            if hasattr(type_, '__contains__'):
                def __contains__(self, item):
                    return item in self._value

            if hasattr(type_, '__del__'):
                def __del__(self):
                    del self._value

            if hasattr(type_, '__delitem__'):
                def __delitem__(self, key):
                    del self._value[key]

            if hasattr(type_, '__delslice__'):
                def __delslice__(self, i, j):
                    del self._value[i:j]

            if hasattr(type_, '__divmod__'):
                def __divmod__(self, other):
                    return divmod(self._value, other)

            if hasattr(type_, '__div__'):
                def __div__(self, other):
                    return self._convert(self._value / other)

            if hasattr(type_, '__eq__'):
                def __eq__(self, other):
                    return self._convert(self._value == other)

            if hasattr(type_, '__float__'):
                def __float__(self):
                    return float(self._value)

            if hasattr(type_, '__floordiv__'):
                def __floordiv__(self, other):
                    return self._convert(self._value // other)

            if hasattr(type_, '__ge__'):
                def __ge__(self, other):
                    return self._convert(self._value >= other)

            if hasattr(type_, '__getitem__'):
                def __getitem__(self, index):
                    return self._convert(self._value[index])

            if hasattr(type_, '__gt__'):
                def __gt__(self, other):
                    return self._convert(self._value > other)

            if hasattr(type_, '__hex__'):
                def __hex__(self):
                    return hex(self._value)

            if hasattr(type_, '__iadd__'):
                def __iadd__(self, other):
                    self._value += other

            if hasattr(type_, '__iand__'):
                def __iand__(self, other):
                    self._value &= other

            if hasattr(type_, '__idiv__'):
                def __idiv__(self, other):
                    self._value /= other

            if hasattr(type_, '__ifloordiv__'):
                def __ifloordiv__(self, other):
                    self._value //= other

            if hasattr(type_, '__ilshift__'):
                def __ilshift__(self, other):
                    self._value <<= other

            if hasattr(type_, '__imod__'):
                def __imod__(self, other):
                    self._value %= other

            if hasattr(type_, '__imul__'):
                def __imul__(self, other):
                    self._value *= other

            if hasattr(type_, '__index__'):
                def __index__(self):
                    return self._convert(self._value.__index__())

            if hasattr(type_, '__int__'):
                def __int__(self):
                    return int(self._value)

            if hasattr(type_, '__invert__'):
                def __invert__(self):
                    return ~self._value

            if hasattr(type_, '__ior__'):
                def __ior__(self, other):
                    self._value |= other

            if hasattr(type_, '__ipow__'):
                def __ipow__(self, power, modulo=None):
                    if modulo:
                        self._value = pow(self._value, power, modulo)
                    else:
                        self._value **= power

            if hasattr(type_, '__irshift__'):
                def __irshift__(self, other):
                    self._value >>= other

            if hasattr(type_, '__isub__'):
                def __isub__(self, other):
                    self._value -= other

            if hasattr(type_, '__iter__'):
                def __iter__(self):
                    return iter(self._value)

            if hasattr(type_, '__itruediv__'):
                def __itruediv__(self, other):
                    return self._convert(other / self._value)

            if hasattr(type_, '__ixor__'):
                def __ixor__(self, other):
                    self._value ^= other

            if hasattr(type_, '__le__'):
                def __le__(self, other):
                    return self._convert(self._value <= other)
                
            if hasattr(type_, '__len__'):
                def __len__(self):
                    return self._convert(len(self._value))

            if hasattr(type_, '__long__'):
                def __long__(self):
                    return long(self._value)

            if hasattr(type_, '__lshift__'):
                def __lshift__(self, other):
                    return self._convert(self._value << other)
                
            if hasattr(type_, '__lt__'):
                def __lt__(self, other):
                    return self._convert(self._value < other)
                
            if hasattr(type_, '__mod__'):
                def __mod__(self, other):
                    return self._convert(self._value % other)
                
            if hasattr(type_, '__mul__'):
                def __mul__(self, other):
                    return self._convert(self._value * other)
                
            if hasattr(type_, '__ne__'):
                def __ne__(self, other):
                    return self._convert(self._value != other)

            if hasattr(type_, '__neg__'):
                def __neg__(self):
                    return self._convert(-self._value)

            if hasattr(type_, '__nonzero__'):
                def __nonzero__(self):
                    return bool(self._value)

            if hasattr(type_, '__oct__'):
                def __oct__(self):
                    return oct(self._value)

            if hasattr(type_, '__or__'):
                def __or__(self, other):
                    return self._convert(self._value | other)

            if hasattr(type_, '__pos__'):
                def __pos__(self):
                    return self._convert(+self._value)

            if hasattr(type_, '__pow__'):
                def __pow__(self, power, modulo=None):
                    if modulo:
                        return self._convert(pow(self._value, power, modulo))
                    else:
                        return self._convert(self._value ** other)
                
            if hasattr(type_, '__radd__'):
                def __radd__(self, other):
                    return self._convert(other + self._value)

            if hasattr(type_, '__rand__'):
                def __rand__(self, other):
                    return self._convert(other & self._value)

            if hasattr(type_, '__rdiv__'):
                def __rdiv__(self, other):
                    return self._convert(other / self._value)

            if hasattr(type_, '__repr__'):
                def __repr__(self):
                    return repr(self._value)

            if hasattr(type_, '__reversed__'):
                def __reversed__(self):
                    return reversed(self._value)

            if hasattr(type_, '__rdivmod__'):
                def __rdivmod__(self, other):
                    return self._convert(divmod(other, self._value))

            if hasattr(type_, '__rfloordiv__'):
                def __rfloordiv__(self, other):
                    return self._convert(other // self._value)

            if hasattr(type_, '__rlshift__'):
                def __rlshift__(self, other):
                    return self._convert(other << self._value)

            if hasattr(type_, '__rmod__'):
                def __rmod__(self, other):
                    return self._convert(other % self._value)

            if hasattr(type_, '__rmul__'):
                def __rmul__(self, other):
                    return self._convert(other * self._value)

            if hasattr(type_, '__ror__'):
                def __ror__(self, other):
                    return self._convert(other | self._value)
                
            if hasattr(type_, '__rpow__'):
                def __rpow__(self, other):
                    return self._convert(other ** self._value)
                
            if hasattr(type_, '__rrshift__'):
                def __rrshift__(self, other):
                    return self._convert(other >> self._value)
                
            if hasattr(type_, '__rshift__'):
                def __rshift__(self, other):
                    return self._convert(self._value >> other)

            if hasattr(type_, '__rsub__'):
                def __rsub__(self, other):
                    return self._convert(other - self._value)

            if hasattr(type_, '__rtruediv__'):
                def __rtruediv__(self, other):
                    return self._convert(other / self._value)

            if hasattr(type_, '__rxor__'):
                def __rxor__(self, other):
                    return self._convert(other ^ self._value)

            if hasattr(type_, '__setitem__'):
                def __setitem__(self, key, value):
                    self._value[key] = value

            if hasattr(type_, '__setslice__'):
                def __setslice__(self, i, j, sequence):
                    self._value[i:j] = sequence

            if hasattr(type_, '__str__'):
                def __str__(self):
                    return str(self._value)

            if hasattr(type_, '__sub__'):
                def __sub__(self, other):
                    return self._convert(self._value - other)
                
            if hasattr(type_, '__truediv__'):
                def __truediv__(self, other):
                    return self._convert(self._value / other)

            if hasattr(type_, '__unicode__'):
                def __unicode__(self):
                    return unicode(self._value)

            if hasattr(type_, '__xor__'):
                def __xor__(self, other):
                    return self._convert(self._value ^ other)

            def __getattr__(self, attr):
                if hasattr(self._value, attr):
                    if callable(getattr(self._value, attr)):
                        def method_wrapper(*args, **kwargs):
                            return self._convert(getattr(self._value, attr)(*args, **kwargs))
                        return method_wrapper
                    else:
                        return getattr(self._value, attr)
                else:
                    raise AttributeError('"{}" object has no attribute "{}"'.format(self.__class__.__name__, attr))
        Wrapped.__name__ = 'Wrapped_' + type_.__name__
        return Wrapped

_wrapped_types = WrapperFactory()

def wrapped(cls):
    """Return wrapped version of the provided class."""
    return _wrapped_types(cls)
