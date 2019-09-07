import sys
import numbers
import math as __mathpy3_math_lib__

if sys.version_info[0] < 3:
    raise Exception("You can't use mathpy3 without Python 3.0 or up!")

def __MATHPY3_REPRESENTATION_METHOD_DEFAULT__(x, sig):
    if sig == -1:
        return str(x)
    return ("%." + str(sig) + "f") % (x)

def __MATHPY3_REPRESENTATION_METHOD_SCIENTIFIC__(x, sig):
    y = x
    exp = 0
    negative = y < 0
    if negative:
        y = -y

    if y >= 1:
        while y >= 10:
            exp += 1
            y /= 10
    elif y > 0 and y < 1:
        while y < 1:
            exp -= 1
            y *= 10

    exp = str(exp)
    if exp[0] != "-":
        exp = "+" + exp

    if sig != -1:
        if negative:
            return "-" + (("%." + str(sig) + "f") % (y)) + "e" + exp
        return (("%." + str(sig) + "f") % (y)) + "e" + exp

    if negative:
        return "-" + str(y) + "e" + exp
    return str(y) + "e" + exp

def __MATHPY3_REPRESENTATION_METHOD_ENGINEERING__(x, sig):
    y = x
    exp = 0
    negative = y < 0
    if negative:
        y = -y

    if y >= 1:
        while y >= 10:
            exp += 1
            y /= 10
        while exp % 3 != 0:
            exp -= 1
            y *= 10
    elif y > 0 and y < 1:
        while y < 1:
            exp -= 1
            y *= 10
        while exp % 3 != 0:
            exp -= 1
            y *= 10

    exp = str(exp)
    if exp[0] != "-":
        exp = "+" + exp

    if sig != -1:
        if negative:
            return "-" + (("%." + str(sig) + "f") % (y)) + "e" + exp
        return (("%." + str(sig) + "f") % (y)) + "e" + exp

    if negative:
        return "-" + str(y) + "e" + exp
    return str(y) + "e" + exp

class Number(numbers.Number):
    REPR_DEFAULT     =     __MATHPY3_REPRESENTATION_METHOD_DEFAULT__
    REPR_SCIENTIFIC  =  __MATHPY3_REPRESENTATION_METHOD_SCIENTIFIC__
    REPR_ENGINEERING = __MATHPY3_REPRESENTATION_METHOD_ENGINEERING__

    @staticmethod
    def pi():
        return Number(3.141592653589793)

    def __init__(self, value=0):
        super().__init__()

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
        return type(self)(self.value_)

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

        return type(self)(result)

    def __sub__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            result = self.value_ - o
        elif isinstance(o, Number):
            result = self.value_ - o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return type(self)(result)

    def __mul__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            result = self.value_ * o
        elif isinstance(o, Number):
            result = self.value_ * o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return type(self)(result)

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

        return type(self)(result)

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

        return type(self)(result)

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

        return type(self)(result)

    def __pow__(self, o):
        result = 0

        if isinstance(o, int) or isinstance(o, float):
            result = self.value_ ** o
        elif isinstance(o, Number):
            result = self.value_ ** o.value_
        else:
            raise TypeError("Tried to pass non-int/float/Number type.")

        return type(self)(result)

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
        return type(self)(-self.value_)

    def __repr__(self):
        return __mathpy3_representation_method__(self.value_, __mathpy3_representation_sigdeci__)

    def __str__(self):
        return __mathpy3_representation_method__(self.value_, __mathpy3_representation_sigdeci__)

def __MATHPY3_ANGLE_TYPE_RADIANS__(measure):
    return measure

def __MATHPY3_ANGLE_TYPE_DEGREES__(measure):
    return (measure/Number.pi().value_)*180

def __MATHPY3_ANGLE_TYPE_GRADIANS__(measure):
    return (measure/Number.pi().value_)*200

class Angle(Number):
    ANG_RADIANS  =   (__MATHPY3_ANGLE_TYPE_RADIANS__, "rad")
    ANG_DEGREES  =   (__MATHPY3_ANGLE_TYPE_DEGREES__, "deg")
    ANG_GRADIANS = (__MATHPY3_ANGLE_TYPE_GRADIANS__, "grad")

    def __init__(self, measure, type_=ANG_RADIANS):
        if type_ == Angle.ANG_DEGREES:
            measure = (measure/180)*Number.pi().value_
        elif type_ == Angle.ANG_GRADIANS:
            measure = (measure/200)*Number.pi().value_
        super().__init__(measure)
        self.type_ = type_

    def to(self, type_):
        return Angle(self.value_, type_)

    def __repr__(self):
        return __mathpy3_representation_method__(self.type_[0](self.value_), __mathpy3_representation_sigdeci__) + self.type_[1]

    def __str__(self):
        return __mathpy3_representation_method__(self.type_[0](self.value_), __mathpy3_representation_sigdeci__) + self.type_[1]

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

def floor(x):
    __is_mathpy3_number__(x)  # Verify x's type
    return Number(int(x.value_))

def ceil(x):
    __is_mathpy3_number__(x)  # Verify x's type
    if (x % 1) != 0:
        return Number(int(x.value_)+1)

    return Number(int(x.value_))

def pow(x, y):
    __is_mathpy3_number__(x)  # Verify x's type
    __is_mathpy3_number__(y)  # Verify y's type

    return x ** y

def sin(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.sin(x)

def cos(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.cos(x)

def tan(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.tan(x)

def asin(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.asin(x)

def acos(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.acos(x)

def atan(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.atan(x)

def sinh(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.sinh(x)

def cosh(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.cosh(x)

def tanh(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.tanh(x)

def asinh(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.asinh(x)

def acosh(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.acosh(x)

def atanh(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return __mathpy3_math_lib__.atanh(x)

def round(x):
    __is_mathpy3_number__(x)  # Verify x's type
    return floor(x.copy()+0.5)

def sqrt(x):
    __is_mathpy3_number__(x)  # Verify x's type

    return Number(__mathpy3_math_lib__.sqrt(x.value_))

def cbrt(x):
    __is_mathpy3_number__(x)  # Verify x's type

    if x >= 0:
        return Number(x ** (1/3))
    return Number(-((-x) ** (1/3)))

def root(x, y):
    __is_mathpy3_number__(x)  # Verify x's type
    __is_mathpy3_number__(y)  # Verify y's type

    if y % 2 == 1:
        if x >= 0:
            return Number(x ** (1/y.value_))
        return Number(-((-x) ** (1/y.value_)))
    if x >= 0:
        return Number(x ** (1/y.value_))
    raise ValueError("math domain error")

def display_mode(mode=Number.REPR_DEFAULT, decimals=-1):
    global __mathpy3_representation_method__
    __mathpy3_representation_method__ = mode
    global __mathpy3_representation_sigdeci__
    __mathpy3_representation_sigdeci__ = decimals
