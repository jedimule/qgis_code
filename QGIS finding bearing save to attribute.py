import math
from PyQt4.QtCore import QVariant

layer = QgsVectorLayer("/Users/andy/Downloads/base data/base_data.shp", "lines", "ogr")
layer.startEditing()

# getting the features of the layer
iter = layer.getFeatures()

# create a new field to hold the bearing
vpr = layer.dataProvider()
vpr.addAttributes([QgsField("bearing", QVariant.Double)])
layer.updateFields()

# getting index of the newly created column
index = layer.fieldNameIndex('bearing')

# calculate the bearing for each line feature
for feats in iter:
    line = feats
    d = QgsDistanceArea()
    d.setEllipsoidalMode(True)
    points = line.geometry().asPolyline()
    first = points[0]
    last = points[-1]

    #calculate bearing from first and last points
    #change from radians to degrees
    r = d.bearing(first, last)
    b = math.degrees(r)
    if b < 0: b += 360

    #updating the column value
    layer.changeAttributeValue(feats.id(), index, b)

# saving the edits to the layer
layer.commitChanges()


# next challenge
# if bearing is of a certain type
# save that geometry to a new layer

# test
