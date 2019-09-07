import sys
import numbers

if sys.version_info[0] < 3:
    raise Exception("You can't use mathpy3 without Python 3.0 or up!")

def __MATHPY3_REPRESENTATION_METHOD_DEFAULT__(x, sig):
    if sig == -1:
        return str(x)
    return ("%." + str(sig) + "f") % x

def __MATHPY3_REPRESENTATION_METHOD_SCIENTIFIC__(x, sig):
    y = x
    exp = 0

    while y >= 10:
        exp += 1
        y /= 10

    return ("%g" % (y)) + "e" + str(exp)

class Number(numbers.Number):
    REPR_DEFAULT    =    __MATHPY3_REPRESENTATION_METHOD_DEFAULT__
    REPR_SCIENTIFIC = __MATHPY3_REPRESENTATION_METHOD_SCIENTIFIC__

    def __init__(self, value=0):
        self.value_ = value
        self.flags = {
            "large": value >= (10**12),
            "small": value > 0 and value < 0.01,
            "zero": value == 0,
            "negative": value < 0
        }

    def set(self, o):
        if isinstance(o, int) or isinstance(o, float):
            self.value_ = o
            self.flags = {
                "large": self.value_ >= (10**12),
                "small": self.value_ > 0 and self.value_ < 0.01,
                "zero": self.value_ == 0,
                "negative": self.value_ < 0
            }
        elif isinstance(o, Number):
            self.value_ = o.value_
            self.flags = {
                "large": self.value_ >= (10**12),
                "small": self.value_ > 0 and self.value_ < 0.01,
                "zero": self.value_ == 0,
                "negative": self.value_ < 0
            }
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return self

    def copy(self):
        return Number(self.value_)

    def large(self):
        return self.flags["large"]

    def small(self):
        return self.flags["small"]

    def zero(self):
        return self.flags["zero"]

    def negative(self):
        return self.flags["negative"]

    def flag(self, name):
        return self.flags.get(name, None)

    def __bool__(self):
        return not self.flags["zero"]

    def __add__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            result = self.value_ + o
        elif isinstance(o, Number):
            result = self.value_ + o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return Number(result)

    def __sub__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            result = self.value_ - o
        elif isinstance(o, Number):
            result = self.value_ - o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return Number(result)

    def __mul__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            result = self.value_ * o
        elif isinstance(o, Number):
            result = self.value_ * o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return Number(result)

    def __truediv__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            if o == 0:
                raise ZeroDivisionError("Divisor was 0")
            result = self.value_ / o
        elif isinstance(o, Number):
            if o.flags["zero"]:
                raise ZeroDivisionError("Divisor was 0")
            result = self.value_ / o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return Number(result)

    def __floordiv__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            if o == 0:
                raise ZeroDivisionError("Divisor was 0")
            result = self.value_ // o
        elif isinstance(o, Number):
            if o.flags["zero"]:
                raise ZeroDivisionError("Divisor was 0")
            result = self.value_ // o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return Number(result)

    def __mod__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            if o == 0:
                raise ZeroDivisionError("Divisor was 0")
            result = self.value_ % o
        elif isinstance(o, Number):
            if o.flags["zero"]:
                raise ZeroDivisionError("Divisor was 0")
            result = self.value_ % o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return Number(result)

    def __pow__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            result = self.value_ ** o
        elif isinstance(o, Number):
            result = self.value_ ** o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return Number(result)

    def __lt__(self, o):
        if isinstance(o, int) or isinstance(o, float):
            return self.value_ < o
        elif isinstance(o, Number):
            return self.value_ < o.value_

        raise TypeError("Tried to pass non-int/float/Number type.")

    def __gt__(self, o):
        if isinstance(o, int) or isinstance(o, float):
            return self.value_ > o
        elif isinstance(o, Number):
            return self.value_ > o.value_

        raise TypeError("Tried to pass non-int/float/Number type.")

    def __le__(self, o):
        if isinstance(o, int) or isinstance(o, float):
            return self.value_ <= o
        elif isinstance(o, Number):
            return self.value_ <= o.value_

        raise TypeError("Tried to pass non-int/float/Number type.")

    def __ge__(self, o):
        if isinstance(o, int) or isinstance(o, float):
            return self.value_ >= o
        elif isinstance(o, Number):
            return self.value_ >= o.value_

        raise TypeError("Tried to pass non-int/float/Number type.")

    def __ne__(self, o):
        if isinstance(o, int) or isinstance(o, float):
            return self.value_ != o
        elif isinstance(o, Number):
            return self.value_ != o.value_

        raise TypeError("Tried to pass non-int/float/Number type.")

    def __eq__(self, o):
        if isinstance(o, int) or isinstance(o, float):
            return self.value_ == o
        elif isinstance(o, Number):
            return self.value_ == o.value_

        raise TypeError("Tried to pass non-int/float/Number type.")

    def __neg__(self):
        return Number(-self.value_)

    def __repr__(self):
        return __mathpy3_representation_method__(self.value_, __mathpy3_representation_sigdeci__)

    def __str__(self):
        return __mathpy3_representation_method__(self.value_, __mathpy3_representation_sigdeci__)

__mathpy3_representation_method__ = Number.REPR_DEFAULT
__mathpy3_representation_sigdeci__ = -1

def __is_mathpy3_number__(value):
    if not isinstance(value, Number):
        raise TypeError("Value was not a mathpy3.Number object.")

    return True

def abs(x):
    __is_mathpy3_number__(x)  # Verify x's type
    if x <= 0:
        return Number(-x)
    return x.copy()

def sign(x):
    __is_mathpy3_number__(x)  # Verify x's type
    if x > 0:
        return Number(1)
    elif x < 0:
        return Number(-1)
    return Number(0)

def display_mode(mode, decimals=-1):
    global __mathpy3_representation_method__
    __mathpy3_representation_method__ = mode
    global __mathpy3_representation_sigdeci__
    __mathpy3_representation_sigdeci__ = decimals
