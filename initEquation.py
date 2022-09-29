# ============================================
# Matrix Calculations 3
# Author: Nora and Ali
# Date: 3/14/22
# License: MIT
# ============================================

class InitEquation(object):
  def __init__(self, a, b, c):
    print("What is your equation? [Ax+By=3]")
    system = input()

    #remove spaces from input string
    system = str(system.replace("+", " "))
    system = str(system.replace(" - ", " -"))
    system = str(system.replace("-", " -"))
    system = str(system.replace("=", " "))

    #remove function signs from input string
    system = str(system.replace("+", ""))
    system = str(system.replace("=", ""))
  
    blacklist = ['x', 'y']
    if all(item in system for item in blacklist):
      #remove x's and y's from input string
      system = str(system.replace("x", ""))
      system = str(system.replace("y", ""))

      #split out number from input string
      a = system.split()[0:1]
      b = system.split()[1:2]
      c = system.split()[2:3]
    
      #strip text from list to strings
      a = ' '.join([str(item) for item in a])
      b = ' '.join([str(item) for item in b])
      c = ' '.join([str(item) for item in c])

      zero = ['.0']
      a = str(a)
      b = str(b)
      c = str(c)

      if all(item in a for item in zero):
        a = a.replace(".0", "")
        self.a = int(a)
      else:
        self.a = float(a)

      if all(item in b for item in zero):
        b = b.replace(".0", "")
        self.b = int(b)
      else:
        self.b = float(b)

      if all(item in c for item in zero):
        c = c.replace(".0", "")
        self.c = int(c)
      else:
        self.c = float(c)

    else:
      print("ERROR: X or Y missing")
      exit()