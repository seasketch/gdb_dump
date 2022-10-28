from distutils.core import setup

setup(name='gdb_dump',
      version='1.0',
      description='Converts all vector layers in a file geodatabase to individual FlatGeobuf files for upload into SeaSketch.',
      author='Chad Burt',
      author_email='chad@underbluewaters.net',
      url='https://github.com/seasketch/gdb_to_fgb',
      install_requires=['alive_progress', 'fiona'],
      scripts=['gdb_dump']
     )