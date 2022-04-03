import sys
import math
import random

RANGE=100

def createArray(n):
  #print("Create Array")
  arrayIn=[]
  for i in range(n):
    arrayIn.append(math.trunc(random.random()*RANGE))
  return(arrayIn)

def bubble(AI):
    #print ("Bubble")
    n = len(AI)
    for npass in range(n-1):
        for i in range(n-1):
            if AI[i]>AI[i+1]:
                aux=AI[i+1]
                AI[i+1]=AI[i]
                AI[i]=aux
    #print(AI)


def improvedBubble(AI):
    #print ("Improved Bubble")
    n = len(AI)
    mod=True
    while(mod==True):
        mod=False
        for i in range(n-1):
            if AI[i]>AI[i+1]:
                aux=AI[i+1]
                AI[i+1]=AI[i]
                AI[i]=aux
                mod=True
    #print(AI)


def selection(AI):
    #print("Selection")
    n=len(AI)
    for npass in range(n-1):
        lowerIndex=npass
        for i in range(npass+1,n):
            if AI[i]<AI[lowerIndex]:
                lowerIndex=i
        aux=AI[npass]
        AI[npass]=AI[lowerIndex]
        AI[lowerIndex]=aux
    #print(AI)



def insertion(AI):
    #print ("Insertion")
    n=len(AI)
    for npass in range(1,n):
        ref=AI[npass]
        for i in range(npass):
            if AI[i]>ref:
                for k in range(npass,i,-1):
                    AI[k]=AI[k-1]
                AI[i]=ref
                break;
    #print(AI)


def quickSort(AI):
    #print ("Quicksort")
    def split(IN):
        LA=[]
        RA=[]
        ref=IN[0]
        for i in range(1,len(IN)):
            if IN[i]<=ref:
                LA.append(IN[i])
            elif IN[i]>ref:
                RA.append(IN[i])
        if len(LA)>1:
            LA=split(LA)
        if len(RA)>1:
            RA=split(RA)
        LA.append(ref)
        LA.extend(RA)
        return(LA)
    
    #print(split(AI))

def pythonSort(AI):
    #print ("PythonSort")
    AI.sort()
    #print(AI)
    
def orderArray(option,n):
  arrayIn=createArray(n)
  #print(arrayIn)

  if option==1:
    bubble(arrayIn)
  elif option==2:
    improvedBubble(arrayIn)
  elif option==3:
    selection(arrayIn)
  elif option==4:
    insertion(arrayIn)
  elif option==5:
    quickSort(arrayIn)
  elif option==6:
    pythonSort(arrayIn)
  else:
    print("Option must be an integer between 1 and 5")




if __name__=="__main__":

  option=int(sys.argv[1])
  n=int(sys.argv[2])
  orderArray(option,n)
  
