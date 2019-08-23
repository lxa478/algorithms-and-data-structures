#!/usr/bin/python

# Helper
incr = lambda x: x + 1


ZERO = lambda f: lambda x: x
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))
FIVE = lambda f: lambda x: f(f(f(f(f(x)))))

TRUE = lambda x: lambda y: x

FALSE = lambda x: lambda y: y

NOT = lambda x: x(FALSE)(TRUE)

AND = lambda x: lambda y: x(y)(x)

OR = lambda x: lambda y: x(x)(y)

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

ADD = lambda x: lambda y: y(SUCC)(x)

MUL = lambda x: lambda y: lambda f: y(x(f))

CONS = lambda a: lambda b: lambda s: s(a)(b)

CAR = lambda p: p(TRUE)

CDR = lambda p: p(FALSE)

T = lambda p: CONS(SUCC(CAR(p)))(CAR(p))

PRED = lambda n: CDR(n(T)(CONS(ZERO)(ZERO)))

SUB = lambda x: lambda y: y(PRED)(x)

ISZERO = lambda n: n(lambda f: FALSE)(TRUE)

LAZY_TRUE = lambda x: lambda y: x()
LAZY_FALSE = lambda x: lambda y: y()
ISZERO = lambda n: n(lambda f: LAZY_FALSE)(LAZY_TRUE)
R = (lambda f: lambda n: ISZERO(n)(lambda: ONE)(lambda: MUL(n)(f(f)(PRED(n)))))
Y = lambda f: (lambda x: f(lambda z:x(x)))(lambda x: f(lambda z:x(x)))
FACT = Y(R)
print FACT(FIVE)(incr)(0)

# Factorial(5) Decomposed
print (lambda f: (lambda x: f(lambda z:x(x)))(lambda x: f(lambda z:x(x))))((lambda f: lambda n: (lambda n: n(lambda f: lambda x: lambda y: y())(lambda x: lambda y: x()))(n)(lambda: lambda f: lambda x: f(x))(lambda: (lambda x: lambda y: lambda f: y(x(f)))(n)(f(f)((lambda n: (lambda p: p(lambda x: lambda y: y))(n(lambda p: (lambda a: lambda b: lambda s: s(a)(b))((lambda n: lambda f: lambda x: f(n(f)(x)))((lambda p: p(lambda x: lambda y: x))(p)))((lambda p: p(lambda x: lambda y: x))(p)))((lambda a: lambda b: lambda s: s(a)(b))(lambda f: lambda x: x)(lambda f: lambda x: x))))(n))))))(lambda f: lambda x: f(f(f(f(f(x))))))(incr)(0)

#print(
#	(lambda f: lambda n: 1 if n==0 else n * f(f)(n-1)) \
#	((lambda f: lambda n: 1 if n==0 else n * f(f)(n-1)))(5))
#
#R = (lambda f: lambda n: 1 if n==0 else n * f(f)(n-1))
#Y = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
#Y = lambda f: (lambda x: f(lambda z:x(x)))(lambda x: f(lambda z:x(x))) # Fix for Python
#
#print Y(R)(5)

factorial = (lambda f: (lambda x: f(lambda z: x(x)))(lambda x: f(lambda z: x(x))))((lambda f: lambda n: 1 if n==0 else n * f(f)(n-1)))
print factorial(5)