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

# Setting up the figure
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Performing autoscaling
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Extracting mass properties and plotting it
volume, cog, inertia = your_mesh.get_mass_properties()
print(f"Volume: {volume},\nPosition of the center of gravity (COG): {cog},\nInertia: {inertia}")
# Show the plot to the screen
pyplot.show()
