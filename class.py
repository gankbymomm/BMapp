import numpy as np
from scipy.optimize import minimize


def object_fc(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 3*x1 + 4*x2 + 5*x3


def equality_constrain(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 0.1*x1 + 0.2*x2 + 0.3*x3 - 90


def equality_constrain1(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 0.3*x1 + 0.4*x2 + 0.2*x3 - 130


def equality_constrain2(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    return 0.02*x1 + 0.01*x2 + 0.03*x3 - 10


bounds_x1 = (0, None)
bounds_x2 = (0, None)
bounds_x3 = (0, None)

bnds = [bounds_x1, bounds_x2, bounds_x3]

constraint1 = {'type': 'ineq', 'fun': equality_constrain}
constraint2 = {'type': 'ineq', 'fun': equality_constrain1}
constraint3 = {'type': 'ineq', 'fun': equality_constrain2}

constraint = [constraint1, constraint2, constraint3]

x0 = [1, 1, 1]

result = minimize(object_fc, x0, method='SLSQP', bounds=bnds, constraints=constraint)

print(result)
