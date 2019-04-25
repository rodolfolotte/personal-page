import gdal

path = "/home/lotte"

image  = gdal.load(path)

show(image)
