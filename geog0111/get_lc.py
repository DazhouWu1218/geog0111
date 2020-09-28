from geog0111.modis import Modis
import gdal
import numpy as np

def get_lc(year,tile,fips):
    '''
    Return LC mask for year,tile,fips
    '''
    kwargs = {
        'tile'      :    tile,
        'product'   :    'MCD12Q1',
    }
    doy = 1
    # get the LC data
    modis = Modis(**kwargs)

    warp_args = {
      'dstNodata'     : 255,
      'format'        : 'MEM',
      'cropToCutline' : True,
      'cutlineWhere'  : f"FIPS='{fips}'",
      'cutlineDSName' : 'data/TM_WORLD_BORDERS-0.3.shp'
    }

    # specify day of year (DOY) and year
    lcfiles = modis.get_modis(year,doy,warp_args=warp_args)
    # get the item we want
    g = gdal.Open(lcfiles['LC_Type3'])
    # error checking
    if not g:
        print(f"cannot open LC file {lcfiles['LC_Type3']}")
        return None
    lc = g.ReadAsArray()
    del g
    
    # in your function, print out the unique values in the 
    # landcover dataset to give some feedback to the user
    print(f"class codes: {np.unique(lc)}")
    return lc

