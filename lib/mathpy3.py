import sys
import numbers

if sys.version_info[0] < 3:
    raise Exception("You can't use mathpy3 without Python 3.0 or up!")

class Number(numbers.Number):
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

    def __repr__(self):
        return repr(self.value_)

    def __str__(self):
        return str(self.value_)
