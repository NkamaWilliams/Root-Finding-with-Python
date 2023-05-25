# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:44:04 2023

@author: Williams
"""

def differentiate(f):
    import sympy as sym
    
    x = sym.Symbol('x')
    f = f.sympify(f(x))
    fprime = f.diff(x)
    return fprime.lambdify([x], fprime)

def myBisection(f, a, b, tol):
    import numpy as np
    
    if np.sign(f(a)) == np.sign(f(b)):
        print(a, b)
        raise Exception("The scalars", a, "and", b, "cannot bound to a root")
    
    m = (a + b) / 2
    
    if np.abs(f(m)) < tol:
        return m
    
    elif np.sign(f(a)) == np.sign(f(m)):
        return myBisection(f, m, b, tol)
    
    elif np.sign(f(b)) == np.sign(f(m)):
        return myBisection(f, a, m, tol)
    
def newtonRaphson(f, fprime, x, tol):
    import numpy as np
    if np.abs(f(x)) < tol:
        return x
    
    x = x - f(x)/fprime(x)
    return newtonRaphson(f, fprime, x, tol)

def mySecant(f, x0, x1, tol, itr):
    import numpy as np
    err = np.abs(x1 - x0)
    x2 = 0
    
    if err > tol:
        for i in range(itr):
            try:
                x2 = x1 - f(x1) * (x0 - x1) / (f(x0) - f(x1))
            except ZeroDivisionError:
                print("Error, cannot divide by zero")
                print(f'x0: {x0}\nx1: {x1}\nf(x0): {f(x0)}\nf(x1): {f(x1)}')
                break
            x0 = x1
            x1 = x2
            err = np.abs(x1 - x0)
            if err < tol:
                print("Reached tolerance at", i)
                break
    
    return x1

def findRoot():
    import ast
    import sympy as sym
    print("Enter the function you want to find the root of below. Ensure 'x' is the variable you use")
    s = "lambda x:"
    s += input("Enter function:")
    f = eval(compile(ast.parse(s, mode='eval'), filename='', mode='eval'))
    try:
        f(0)
    except:
        raise Exception("Invalid function! Did you use the variable x?")
    
    print("Which method do you want to use? Enter the corresponding value")
    print("Bisection: 1")
    print("Newton Raphson: 2")
    print("Secant: 3")
    
    method = int(input("Enter method value:"))
    
    if method == 1:
        a = int(input("Enter x1:"))
        b = int(input("Enter x2:"))
        tol = float(input("Enter tolerance:"))
        print(myBisection(f, a, b, tol))
        return
    elif method == 2:
        x = int(input("Enter x:"))
        tol = float(input("Enter tolerance:"))
        x1 = sym.Symbol('x')
        fprime = differentiate(f)
        print(newtonRaphson(f, fprime, x, tol))
        return
    elif method == 3:
        x0 = int(input("Enter x0:"))
        x1 = int(input("Enter x1:"))
        tol = float(input("Enter tolerance:"))
        itr = int(input("Enter the number of iterations:"))
        print(mySecant(f, x0, x1, tol, itr))
        return
    else:
        print("That is an invalid selection")
        return
    return "DONE!"

findRoot()