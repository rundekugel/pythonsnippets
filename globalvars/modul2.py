#!/usr/bin/env python
"""globals variables demo"""

import globalsContainer

def f1():
  gc = globalsContainer
  print("m2.f1:",gc.varA1, gc.myglobals.varC1)
  gc.varA1 = 711
  gc.myglobals.varC1 =712
  
  
def f2():
  gc = globalsContainer
  print("m2.f2:",gc.varA1, gc.myglobals.varC1,globalsContainer.myglobals)
  gc.varA1 = 721
  gc.myglobals.varC1 =722

def main():
  print("m2.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  f1()
  print("m2.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  f2()
  print("m2.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1,globalsContainer.myglobals)
  
