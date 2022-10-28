# gdb_dump

Command line utility that exports all vector layers of an Esri File Geodatabase
into individual FlatGeobuf files. The McClintock Lab has in the past organized
layers for many of our projects using File Geodatabases but these multi-layer
archives cannot be uploaded directly to SeaSketch. Individual FlatGeobuf files
can be uploaded directly to SeaSketch Next (without zip'ing, like shapefile),
and can be opened for debugging in QGIS.


## Installation

python3 -m pip install "gdb_dump @ git+https://github.com/seasketch/gdb_dump"