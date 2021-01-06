
'''
Generate a random number
list and perform a binary search as a loop
SH 2019-02-03, based on earlier by GW, NH and more.
'''

###########################################
import argparse
import numpy as np

###########################################

def getCmdArgs():
  '''
  Read commandline arguments
  '''
  p = argparse.ArgumentParser(description=("Demonstrating of sorting a list of numbers"))
  p.add_argument("--len", dest ="n", type=int, default=100, help=("Length of array"))
  p.add_argument("--val", dest ="x", type=float, default=0.5, help=("Value to search for"))
  cmdargs = p.parse_args()
  return cmdargs


###########################################

def newMidInd(sInd,eInd):
  '''
  Set a new mid index
  '''
  return((eInd-sInd)//2+sInd) # the point halfway between start and end bounds. Note that sInd is added
                              # to keep aligned with the sortedList array
                              # // divides and rounds two numbers, ensuring that the output is a whole number


###########################################

def binarySearch(sortedList,x):
  '''
  Perform a binary search for
  a given value
  '''
  # identify a mid position
  sInd=0                  # search bounds start index
  eInd=len(sortedList)-1  # search bounds end index
  midInd=newMidInd(sInd,eInd)

  # the loop
  while((eInd-sInd)>1):  # whilst there are still elements in our area of interest, keep searching
    print("testing",x,sortedList[midInd],"unsearched",eInd-sInd)
    if(sortedList[midInd]>x):  # value too high, look to the left. We still, haven't found, what we're looking for
      eInd=midInd       # update the search bounds
      midInd=newMidInd(sInd,eInd)
    elif(sortedList[midInd]<x):  # value too low, look to the right. We still, haven't found, what we're looking for
      sInd=midInd       # update the search bounds
      midInd=newMidInd(sInd,eInd)
    else:          # we have found the right value. Break from the loop
      break

  print(x,"found at",midInd)   # write the answer to the screen


###########################################

if __name__ == '__main__':
  '''
  Main block
  '''
  cmdargs=getCmdArgs()
  # generate list of random numbers
  ranList=np.random.rand(cmdargs.n)
  # sort the list. Use the built in numpy function
  sortedList=np.sort(ranList)
  # binary search
  binarySearch(sortedList,cmdargs.x)

