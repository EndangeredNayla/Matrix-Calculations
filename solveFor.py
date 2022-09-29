# ============================================
# Matrix Calculations 3
# Author: Nora and Ali
# Date: 3/14/22
# License: MIT
# ============================================
from determinant import Determinant
from linearEquation import LinearEquation


def SolveForX(firstEq, secondEq):
  
  # make new holder eqs
  eq1x = LinearEquation() 
  eq2x = LinearEquation()

  # fill the x-position with the constant terms, and y-position with y-terms (etc) solve
  eq1x.a = firstEq.c
  eq1x.b = firstEq.b
  eq2x.a = secondEq.c
  eq2x.b = secondEq.b

  #take det of firstEq, secondEq. call it detA
  detA = Determinant(firstEq, secondEq)
    
  #take det of eq1x and eq2x. Call this...B?
  detB =  Determinant(eq1x, eq2x)

  # x = B / detA. Return x
  x = detB / detA

  zero = ['.0']
  x = str(x)
  if all(item in x for item in zero):
    x = x.replace(".0", "")
    x = int(x)
  else:
    x = float(x)
    
  return x

def SolveForY(firstEq, secondEq):
  
  # make new holder eqs
  eq1y = LinearEquation() 
  eq2y = LinearEquation()

  # fill the x-position with the constant terms, and y-position with y-terms (etc) solve
  eq1y.a = firstEq.a
  eq1y.b = firstEq.c
  eq2y.a = secondEq.a
  eq2y.b = secondEq.c

  #take det of firstEq, secondEq. call it detA
  detA = Determinant(firstEq, secondEq)
    
  #take det of eq1x and eq2x. Call this...B?
  detB =  Determinant(eq1y, eq2y)
  

  # y = B / detA. Return y
  y = detB / detA

  zero = ['.0']
  y = str(y)
  if all(item in y for item in zero):
    y = y.replace(".0", "")
    y = int(y)
  else:
    y = float(y)

  return y