# ============================================
# Matrix Calculations 3
# Author: Nora and Ali
# Date: 3/14/22
# License: MIT
# ============================================

# calculate a determinant
def Determinant(firstEq, secondEq):
  d = (firstEq.a * secondEq.b - firstEq.b * secondEq.a)
  return d