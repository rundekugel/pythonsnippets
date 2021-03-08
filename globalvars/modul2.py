#!/usr/bin/env python
"""globals variables demo"""

import globalsContainer
import globalsContainerSimple

def f1():
  gc = globalsContainer
  print("m2.f1:",gc.varA1, gc.myglobals.varC1, globalsContainerSimple.testvar)
  print("m2.f1 change values")
  gc.varA1 = 711
  gc.myglobals.varC1 =712
  globalsContainerSimple.testvar=2.1
  
  
def f2():
  gc = globalsContainer
  print("m2.f2:",gc.varA1, gc.myglobals.varC1,globalsContainer.myglobals, globalsContainerSimple.testvar)
  print("m2.f2 change values")
  gc.varA1 = 721
  gc.myglobals.varC1 =722
  globalsContainerSimple.f2="hi"
  globalsContainerSimple.testvar=2.2
  
def returnNoS(mylist)  :
  r=[]
  for i in mylist:
    try:
      if i[0] == "_":
        continue
    except:
      pass
    r.append(i)
  return r

def main():
  globalsContainerSimple.varFromM2 = "init2"
  print("m2.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1, globalsContainerSimple.testvar)
  f1()
  print("m2.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1)
  f2()
  print("m2.m:",globalsContainer.varA1, globalsContainer.myglobals.varC1,globalsContainer.myglobals, globalsContainerSimple.testvar)
  print("from m2 globalsContainerSimple dir: ",returnNoS(dir(globalsContainerSimple)))
  
