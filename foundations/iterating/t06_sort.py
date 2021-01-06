
'''
Generate a random number
list and sort
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
  cmdargs = p.parse_args()
  return cmdargs


###########################################

def sortList(x):
  '''
  Sort a list of numbers
  known as "bubble sort"
  Note that this is a very
  inefficient algorithm,
  but it is correct
  '''
  for i in range (len(x)-1):  # select origin element
    for k in range(i+1, len(x)):  # select element to test against
      if (x[i]>x[k]):   # compare the elements
        temp=x[k]       # if out of order, swap
        x[k]=x[i]
        x[i]=temp       # the swap requires a temporary variable to prevent x[k] being lost


###########################################

def writeArray(x):
  '''
  Write a list out
  '''
  for i in range(0,len(x)):
    print(i,x[i])


###########################################

if __name__ == '__main__':
  '''
  Main block
  '''
  cmdargs=getCmdArgs()
  # generate list of random numbers
  ranList=np.random.rand(cmdargs.n)
  # sort the list
  sortList(ranList)
  # write out
  writeArray(ranList)

