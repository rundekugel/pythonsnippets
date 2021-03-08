#!/usr/bin/env python
"""globals variables demo"""

import globalsContainer
import globalsContainerSimple
import modul2

def f1():
  gc = globalsContainer
  print("m1.f1:",gc.varA1, gc.myglobals.varC1, globalsContainerSimple.testvar)
  print("m1.f1 change values")
  gc.varA1 = 111
  gc.myglobals.varC1 =112
  globalsContainerSimple.testvar = 1.1
  
  
def f2():
  gc = globalsContainer
  print("m1.f2:",gc.varA1, gc.myglobals.varC1, globalsContainerSimple.testvar)
  print("m1.f2 change values")
  gc.varA1 = 121
  gc.myglobals.varC1 =122
  globalsContainerSimple.testvar = 1.2

def main():
  print("Verify the address of the class myglobals, because it's used as static class, \
       all the modules access the same variables address.)")
  print("m1:", globalsContainer.myglobals.varCHallo, globalsContainer.myglobals, modul2.globalsContainer.myglobals )
  gcInstance = globalsContainer.myglobals() # create an instance
  globalsContainerSimple.testvar = "init"
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1, globalsContainerSimple.testvar)
  gcInstance.varA1 = 0.1
  gcInstance.varC1 = 0.2
  print("m1.m value of instance: ", gcInstance.varC1)
  f1()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1, globalsContainerSimple.testvar)
  f2()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1, globalsContainerSimple.testvar)
  
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  modul2.f1()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  modul2.f2()
  print("m1.m:",modul2.globalsContainer.varA1, modul2.globalsContainer.myglobals.varC1)
  modul2.main()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  globalsContainer.varA1, globalsContainer.myglobals.varC1 = 91,92
  print("m1.m change values")
  modul2.main()
  print("m1.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1, globalsContainerSimple.testvar)
  print("m1.m value of instance: ", gcInstance.varC1)
  
main()

