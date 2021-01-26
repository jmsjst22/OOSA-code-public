
'''
An example of how to use the 
LVIS python scripts
'''

from processLVIS import lvisGround



if __name__=="__main__":
  '''Main block'''

  filename='/geos/netdata/avtrain/data/3d/oosa/week4/lvis_antarctica/ILVIS1B_AQ2015_1014_R1605_070717.h5'

  # create instance of class with "onlyBounds" flag
  b=lvisGround(filename,onlyBounds=True)

  # to make a MWE,
  # from the total file bounds
  # choose a spatial subset
  x0=b.bounds[0]
  y0=b.bounds[1]
  x1=(b.bounds[2]-b.bounds[0])/20+b.bounds[0]
  y1=(b.bounds[3]-b.bounds[1])/20+b.bounds[1]


  # read in all data within our spatial subset
  lvis=lvisGround(filename,minX=x0,minY=y0,maxX=x1,maxY=y1)

  # set elevation
  lvis.setElevations()

  # plot up some waveforms

