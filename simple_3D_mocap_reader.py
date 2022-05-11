# first import the blender python module
import bpy
import csv
import numpy as np

mocap_file = "PATH/TO/FILE.csv"

coords = []

with open(mocap_file) as f:
    for l, line in enumerate(f):
        if l < 2:
            # used to skip header and empty row
            pass
        else:
            row_elems = line.split(",")
            coords.append(row_elems[11:20])

# now let's create an empty object for every retrieved triplet
coords_np = np.array(coords)
coords_np = coords_np.astype(float)

num_trajectories = int(coords_np.shape[1] / 3)

print(num_trajectories)


for t in range(num_trajectories):
    # add empty
    bpy.ops.object.add(radius=1.0, type='EMPTY', 
                       enter_editmode=False, align='WORLD', 
                       location=(t, t, t), 
                       rotation=(0.0, 0.0, 0.0), 
                       scale=(1.0, 1.0, 1.0))
    object_name = "Empty"
    # poorly written, expand on this in case you have more trajectories
    # alternatively rename the generated empties instead.
    if t > 0:
        object_name += ".00" + str(t)
    empty_to_animate = bpy.context.scene.objects[object_name]
    
    for frame, pos in enumerate(coords_np[:, t * num_trajectories : t * num_trajectories + 3]):
        # using inverted Y axis coordinates
        empty_to_animate.location = [pos[0], -pos[1], pos[2]]
        # Set the keyframe with that location at a desired frame 
        empty_to_animate.keyframe_insert(data_path="location", frame=frame + 1)
    