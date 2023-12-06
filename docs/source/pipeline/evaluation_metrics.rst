WM Bundles Evaluation
========================

For each bundle, subject and session, 3 types of measurements are extracted using the tractometry flow pipeline:

- Bundle-averaged
- Bundle-profile or track-profile
- Bundle-streamline measures

The evaluation of the white matter bundles measures is performed using the `Tractometry Flow`_ pipeline.

.. note::

   `Tractometry Flow`_ pipeline remove of any streamline that are out of the volume, no negative coordinate and no above volume dimension coordinate are possible.

 .. _Tractometry Flow: https://github.com/scilus/tractometry_flow

Bundle-streamline measures
  Three measures of streamlines are extracted for each bundle:

   - The bundle **volume**, in mm3, is estimated by counting the number of voxels occupied by the bundle and multiplying it by the volume of a single voxel.
   - The average **length**, em mm, is estimated by averaging the length of all the streamlines of the bundle.
   - The **number** of streamlines in a bundle (**count**).

Bundle-averaged
  For each measures, **mean** is computed by averaging the measures value of all voxels occupied by the bundle.

  .. figure:: pipelines.jpg
     :align: center

     Figure 1. Representation of the pipelines used for the evaluation of the white matter bundles.

Bundle-profile
  To generate the bundle-profile (also called track-profiles), `Tractometry Flow`_ first compute a centroid which is then resampled to 20 equidistant points. Each voxel will have the section label (1 to 20) of its closest centroid point (Figure 2).
  For each section, **mean** is computed by averaging the measures value of all voxels occupied by the section (label, Figure 1).

  .. figure:: bundles_profiling.png
     :align: center
     :width: 700

     Figure 2. Representation of  white matter major bundle models resampled  into 20 segments for illustration. Left and right have been merged. The colors displayed on the bundles represent the section numbers from 1 (blue) to 20 (red).


Streamlines metrics generated
-----------------------------
Table describe all streamlines metrics which will be generated for each bundle.

+-----------------+-----------------------+
| Tools           | Streamline metrics    |
+=================+=======================+
| RBXflow         | Count (n)             |
+-----------------+-----------------------+
|                 | Volume (mm3)          |
+-----------------+-----------------------+
|                 | Length (mm)           |
+-----------------+-----------------------+

MRI measurements generated
-------------------------------
Table describe all measure maps which will be evaluated.

+-------------------------------+-------------------------------------------+
| Tools                         | MRI measurements (mean)                   |
+===============================+===========================================+
| Tractoflow - DTI              | Fractional anisotropy (FA)                |
+-------------------------------+--------------------+----------------------+
|                               | Mean Diffusivity (MD)                     |
+-------------------------------+--------------------+----------------------+
|                               | Radial Diffusivity (AD)                   |
+-------------------------------+--------------------+----------------------+
|                               | Axial Diffusivity (AD)                    |
+-------------------------------+--------------------+----------------------+
| Tractoflow - DTI-FW corrected | Fractional anisotropy tissue (FAt)        |
+-------------------------------+--------------------+----------------------+
|                               | Mean Diffusivity tissue (MDt)             |
+-------------------------------+--------------------+----------------------+
|                               | Radial Diffusivity tissue (ADt)           |
+-------------------------------+--------------------+----------------------+
|                               | Axial Diffusivity tissue (ADt)            |
+-------------------------------+--------------------+----------------------+
| Tractoflow - FW               | Free water (FW)                           |
+-------------------------------+--------------------+----------------------+
| Tractoflow - FODF             | Apparent fiber density total (AFD total)  |
+-------------------------------+--------------------+----------------------+
|                               | Number of fober direction (NuFO)          |
+-------------------------------+--------------------+----------------------+
| NODDI flow                    | Intra-cellular volume fraction (ICvf)     |
+-------------------------------+--------------------+----------------------+
|                               | Extra-cellular volume fraction (ECvf)     |
+-------------------------------+--------------------+----------------------+
|                               | Isotropic volume fraction (ISOvf)         |
+-------------------------------+--------------------+----------------------+
|                               | Orientation direction (OD)                |
+-------------------------------+--------------------+----------------------+
| ihMT flow                     | ihMT ratio (ihMTR)                        |
+-------------------------------+--------------------+----------------------+
|                               | ihMT delta R1 saturation (ihMTsat)        |
+-------------------------------+--------------------+----------------------+
|                               | MT ratio (MTR)                            |
+-------------------------------+--------------------+----------------------+
|                               | MT saturation (MTsat)                     |
+-------------------------------+--------------------+----------------------+