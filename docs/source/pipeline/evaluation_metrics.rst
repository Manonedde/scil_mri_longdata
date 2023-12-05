WM Bundles Evaluation
========================

For each bundle, subject and session, 3 types of measurements are extracted using the tractometry flow pipeline: 
- Bundle-averaged
- Bundle-profile or track-profile
- Bundle-streamline measures

The evaluation of the white matter bundles measures is performed using the `Tractometry Flow`_ pipeline.

.. note::

   This pipeline remove of any streamline that are out of the volume, no negative coordinate and no above volume dimension coordinate are possible.


Bundle-streamline measures
---------------------------

Three measures of streamlines are extracted for each bundle:
- The bundle **volume**, in mm3, is estimated by counting the number of voxels occupied by the bundle and multiplying it by the volume of a single voxel.
- The average **length**, em mm, is estimated by averaging the length of all the streamlines of the bundle.
- The **number** of streamlines in a bundle (count).


Bundle-averaged
---------------

For each measures, **mean** is computed by averaging the measures value of all voxels occupied by the bundle.

.. figure:: pipelines.jpg
   :align: center
   :width: 700

   Figure 1. Representation of the pipelines used for the evaluation of the white matter bundles.


Bundle-profile
---------------

To generate the bundle-profile (also called track-profiles), `Tractometry Flow`_ first compute a centroid which is then resampled to 20 equidistant points by streamline. Each voxel will have the section label (1 to 20) of its closest centroid point (Figure 2).

For each section, **mean** is computed by averaging the measures value of all voxels occupied by the section (label).


.. figure:: bundles_profiling.png
   :align: center
   :width: 700

   Figure 2. Representation of  white matter major bundle models resampled  into 10 segments for illustration. Left and right have been merged. The colors displayed on the bundles represent the section numbers from 1 (blue) to 10 (red).



 .. _Tractometry Flow: https://github.com/scilus/tractometry_flow
