"""
    Working with .stl file(solidworks) in python
    Packages: numpy-stl, mpl_toolkits, matplotlib
    @author: Milad Sadeghi DM - EverLookNeverSee@GiHub
"""


from stl import mesh
from matplotlib import pyplot
from mpl_toolkits import mplot3d

# stl file path
path = "/home/elns/Projects/stl_stuff/test_stl_files/Eiffel_tower_sample.STL"
# Loading stl file
your_mesh = mesh.Mesh.from_file(path, calculate_normals=False, speedups=True)
