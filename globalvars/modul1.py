#!/usr/bin/env python
"""globals variables demo"""

import globalsContainer
import modul2

def f1():
  gc = globalsContainer
  print("m1.f1:",gc.varA1, gc.myglobals.varC1)
  gc.varA1 = 111
  gc.myglobals.varC1 =112
  
  
def f2():
  gc = globalsContainer
  print("m1.f2:",gc.varA1, gc.myglobals.varC1)
  gc.varA1 = 121
  gc.myglobals.varC1 =122

def main():
  print("m1:", globalsContainer.myglobals.varCHallo, globalsContainer.myglobals, modul2.globalsContainer.myglobals )
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  f1()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  f2()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  modul2.f1()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  modul2.f2()
  print("m1.m:",modul2.globalsContainer.varA1, modul2.globalsContainer.myglobals.varC1)
  modul2.main()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  globalsContainer.varA1, globalsContainer.myglobals.varC1 = 91,92
  modul2.main()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  
main()
