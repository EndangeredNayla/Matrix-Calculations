# ============================================
# Matrix Calculations 3
# Author: Nora and Ali
# Date: 3/10/22
# License: MIT
# ============================================

#from file initEquation import class InitEquation
from initEquation import InitEquation  

#from file linearEquation import class LinearEquation
from linearEquation import LinearEquation

#from file splash import function splash
from splash import splash

#from file solveFor import function SolveForX, and SolveForY
from solveFor import SolveForX, SolveForY

#====================
#    MAIN PROGRAM   |
#====================
splash()

#should create eq1 with all 0's
eq1 = LinearEquation()
eq2 = LinearEquation()

#replaces 0's with user input
eq1 = InitEquation(eq1.a, eq1.b, eq1.c)
eq2 = InitEquation(eq2.a, eq2.b, eq2.c)

X = SolveForX(eq1, eq2)
Y = SolveForY(eq1, eq2)

print("X = " + str(X))
print("Y = " + str(Y))