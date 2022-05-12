# Blender MoCapReader

_Reading 3D motion capture data to animate meshes_

<img src=images/mandible_comp.gif width="500">

# How to MCR

The process is relatively straightforward as soon as you know your way around Blender and pick up the two or three shortcuts.
Just be sure to closely follow the steps below regarding the order in which elements need to be selected to assign the desired dependency.

## load keypoints into Blender

First, open a new Blender file and head to the **Scripting** tab. Here, load the **simple_3D_mocap_reader.py** script. 

**DON'T** run the script yet. 

<img src=images/0.JPG width="600">

We need to clean the scene first to see what is being added. Move your mouse into the **3D Viewer** panel on the top left.

Then press **A**, then press **delete** to remove all elements from the scene.

<img src=images/1_A.JPG width="400">
<img src=images/1_B.JPG width="400">

Now, we can load the keypoints from the input **.csv** file. Enter the **absolute** path to your file in the loaded script.

<img src=images/2.JPG width="700">

Double check the coordinate system of the imported coordinates in **line 44**. In this case, we invert the **y axis**

<img src=images/3.JPG width="700">

Once all is set up, hit **execute** (the right facing arrow on the top right above the loaded script). If everything worked according to plan, you should now see the imported keypoints as keyframed **empty** objects in the **3D viewport**

<img src=images/4_A.JPG width="400">

These empty objects are generated in the order they appear in the input .csv file.

<img src=images/4_B.JPG width="400">

Now, head back to the **Layout** tab.

<img src=images/5.JPG width="500">

## Assign Armature

We need to create an Armature tied to the imported keypoints to anchor the mesh to them. The Armature consists of **n - 1** bones, with **n** being the number of keypoints (and thus empties). We parent the base of the Armature to one of the empty objects and have the extending bones span between all empties at a fixed length, tracking their location.

Begin by **snapping** the **cursor** to one of the empty objects. The order does not matter. However, you mustn't move any of the keyframes in the **Timeline**, or **Dope Sheet** and perform all the following actions while at **Frame 1**. 

Select the **empty** object, which will become our base, by **left clicking** it. Then **right click** the selected **empty** and choose **Snap > Cursor to Selected**

<img src=images/6.JPG width="600">

Now create an Armature at this point by pressing **shift + A** and selecting **Armature** from the drop-down menu

<img src=images/7.JPG width="600">

Next, switch to **Edit Mode** by pressing **tab** or selecting **Edit Mode** from the top left menu. To make moving the bone tip to an adjacent empty object easier, enable **Snap to Vertex** by clicking on the **magnet** symbol at the top of the viewport.

<img src=images/8.JPG width="600">

Select the **tip**, and ONLY the **tip**, of the bone and press **G** to move it. You may need to change the orientation by holding down the mouse wheel to make snapping to the correct spot easier. Once the tip has snapped to one of the other empty objects, confirm the action by clicking the **Left mouse button**

<img src=images/9.JPG width="600">

Now, create additional bones from the base of the original bone in the Armature to connect to the remaining empty objects. Select the **base** of the bone and press **E** to extrude another bone. Move its tip to the desired empty and confirm your choice with the **left mouse button** again.

<img src=images/10.JPG width="600">

Switch back to **Object Mode** by selecting it from the top left drop-down menu. Now we parent the created Armature to the empty located at its base. It is essential to follow the order of these steps to arrive at the desired hierarchy.

1. **Left click** the Armature
2. Hold **shift** and **Left click** the empty at the base
3. Press **ctrl + P** and **Set parent to Object**

<img src=images/11.JPG width="600">

Now we assign **Bone constraints** to track the non-parented empty objects.

To do so, having selected the Armature, switch to **Pose Mode**. 

<img src=images/12.JPG width="600">

From the property tab on the right, select **Bone Constraint Properties** (in Blender 2.92, it is the second entry from the bottom). Select **one** of the bones and add a new **Track To** bone constraint. This constraint will lead to the bone always pointing towards the location of the empty without changing its scale.

<img src=images/13.JPG width="600">

In the newly created **Track To** constraint, set the **Target** to the **empty** object the bone is pointing to, and select **Y** as the **Track Axis** and **Z** as the **Up** orientation. Leave all other values unchanged, and ensure the **Influence** is set to 1.000.

<img src=images/14.JPG width="600">

Select the other bone(s) and repeat the process until all bones have been assigned one **empty**.

<img src=images/15.JPG width="600">

Apply the new Armature configuration as the **default pose** to avoid deforming the **mesh** in the final step.
While in **Pose Mode**, select **Pose** > **Apply** > **Apply Pose as Rest Pose**

## Importing and parenting the generated mesh

Switch back to **Object Mode** and import the mesh you wish to assign to the Armature. Simply select **File** > **Import** > **Wavefront (.obj)** or whichever format you used to export your mesh.

<img src=images/18.JPG width="600">
<img src=images/19.JPG width="600">

To make moving your imported mesh in the scene easier, select your mesh, then **Right click** on it and **Set Origin** > **Origin to Centre of Mass (Surface)**

<img src=images/20.JPG width="600">

Moving your mesh to the desired position may involve a combination of **moving**, **rotating**, and potentially **scaling** your mesh. Use the following shortcuts to make the process, and thus your life, easier:

* **G** - Move mesh
* **R** - Rotate mesh
* **S** - Scale mesh

After pressing any of these keys, you can additionally constrain the manipulation by pressing any of the following:

* **X**, **Y**, or **Z** - constrain the manipulation to a single axis
* holding **shift** - make smaller adjustments
* holding **ctrl** - make incremental adjustments

Again, all changes are confirmed by pressing the **Left Mouse Button** or cancelled by pressing the **Left Mouse Button**

<img src=images/21.JPG width="600">

Once your mesh is in the desired position, lined up with its respective keypoints, all that is left to do is **parent** the mesh to the Armature. The order is important:

1. **Left click** the mesh
2. Hold **shift** and **Left click** the Armature
3. Press **ctrl + P** and **Armature Deform** > **With Automatic Weights**

<img src=images/22.JPG width="600">

You did it! Well hopefully. 

<img src=images/mandible_comp.gif width="500" height="250">

You can now scrub through the animation by dragging the blue frame indicator in the timeline

<img src=images/23.JPG width="400">


In case you have any issues using these shortcuts on a Mac, this is the point where you realise that you should have just bought a PC instead. Alternatively, if you are stubborn and prefer Apple products, head over to [this website](https://tutorialslink.com/shortcut-keys/most-used-keyboard-shortcut-keys-in-Blender-for-mac-os) for some pointers.
