Bundles Evaluation
======================

For each subject and session, the evaluation of the white matter bundles 
measures is performed using the `Tractometry Flow`_ pipeline.

Three types of measurements are extracted for each bundle:

- Bundle-streamline measures
- Bundle-averaged
- Bundle-profile (or track-profile)


Bundle-streamline measures
  Three measures are extracted from the streamlines for each bundle (Figure 1):

   - The bundle **volume**, in mm3, is estimated by counting the number of voxels occupied by the bundle and multiplying it by the volume of a single voxel.
   - The bundle average **length**, in mm, is estimated by averaging the length of all the streamlines of the bundle.
   - The bundle streamline **count**, i.e. the number of streamlines in a bundle.
  
  .. note::

   `Tractometry Flow`_ pipeline removes any streamline that falls out of the 
   volume, i.e. no negative coordinate or coordinates outside the volume's dimension are possible.


Bundle-averaged
  For each measures, the bundle-averaged **mean** is computed by averaging a specific measure value for all voxels occupied by the bundle (Figure 1).

  .. figure:: Figure_data_extraction_streamlines_average.png
     :align: center
     :width: 750

     Figure 1. Representation of the extraction of Bundle-streamlines and Bundle-average measures.

Bundle-profile
  To generate the bundle-profile (also called track-profiles), `Tractometry Flow`_ resamples its centroid into **20 equidistant points**.
  Then, each voxel is assigned to the section label (1 to 20) of its closest centroid point (Figure 2).

  .. figure:: bundles_profiling.png
     :align: center
     :width: 750

     Figure 2. Representation of  white matter major bundle models resampled  into 20 segments for illustration.
     Left and right have been merged. The colors displayed on the bundles represent the section numbers from 1 (blue) to 20 (red).

  For each section, **mean** is computed by averaging the measures value of all voxels occupied by the section (label, Figure 1).
  Finally, a tract profile is extracted for each combination of measurements and bundles (Figure 3).

  .. figure:: Figure_data_extraction_profile.png
     :align: center
     :width: 700

     Figure 3. Representation of the extraction of Bundle-profile measures.

.. note::

   Mean measurement values can be computed either by session i.e. including all subjects for one session, 
   or by averaging all sessions and all subjects (average).


Visualization
----------------

Results are displayed using `Plotly`_'s interactive plots. Click on the legend to select and/or deselect plot elements.
Colors represent bundle or MRI measurements.

For most figures, the slider can represent :

 - sessions (Session1, Session 2, ...) and/or the average of all sessions (average)
 - MRI measurements

 .. _Plotly: https://plotly.com/
 .. _Tractometry Flow: https://github.com/scilus/tractometry_flow


Streamlines metrics generated
-----------------------------
Table describe all streamlines metrics generated for each bundle.

+-------------+---------------------+
|    Tools    | Streamline metrics  |
+=============+=====================+
|             | Volume (mm3)        |
+             +---------------------+
|   RBXflow   | Count (n)           |
+             +---------------------+
|             | Length (mm)         |
+-------------+---------------------+

MRI measurements generated
-------------------------------
Table describe all measure maps generated.

+-------------------------------+--------------------------------------------------+
|            Tools              | MRI measurements (mean)                          |
+===============================+==================================================+
|                               | Fractional anisotropy (FA)                       |
+                               +--------------------------------------------------+
|                               | Mean Diffusivity (MD) s/mm2                      |
+  Tractoflow - DTI             +--------------------------------------------------+
|                               | Radial Diffusivity (RD) s/mm2                    |
+                               +--------------------------------------------------+
|                               | Axial Diffusivity (AD) s/mm2                     |
+-------------------------------+--------------------------------------------------+
|                               | Fractional anisotropy tissue (FA-FWcorrected)    |
+                               +--------------------------------------------------+
|  Freewater Flow               | Mean Diffusivity tissue (MD-FWcorrected) s/mm2   |
+  DTI-FW corrected             +--------------------------------------------------+
|                               | Radial Diffusivity tissue (RD-FWcorrected) s/mm2 |
+                               +--------------------------------------------------+
|                               | Axial Diffusivity tissue (AD-FWcorrected) s/mm2  |
+-------------------------------+--------------------------------------------------+
|  Freewater Flow - FW          | Free water (FW)                                  |
+-------------------------------+--------------------------------------------------+
|                               | Total Apparent fiber density (AFD total)         |
+  Tractoflow - FODF            +--------------------------------------------------+
|                               | Number of fober direction (NuFO)                 |
+-------------------------------+--------------------------------------------------+
|                               | Intra-cellular volume fraction (ICvf)            |
+                               +--------------------------------------------------+
|                               | Extra-cellular volume fraction (ECvf)            |
+  NODDI Flow                   +--------------------------------------------------+
|                               | Isotropic volume fraction (ISOvf)                |
+                               +--------------------------------------------------+
|                               | Orientation direction (OD)                       |
+-------------------------------+--------------------------------------------------+
|                               | ihMT ratio (ihMTR)                               |
+                               +--------------------------------------------------+
|                               | ihMT delta R1 saturation (ihMTsat)               |
+  ihMT Flow                    +--------------------------------------------------+
|                               | MT ratio (MTR)                                   |
+                               +--------------------------------------------------+
|                               | MT saturation (MTsat)                            |
+-------------------------------+--------------------------------------------------+


* Add description of metrics is usefull ? 

+-------------------------------+-----------------------------------------------+-------------------------------------------------------------------------+
| Tools                         | MRI measurements (mean)                       |                      Description                                        |
+===============================+===============================================+=========================================================================+
|                               | Fractional anisotropy (FA)                    | Anisotropy measure of the diffusion tensor                              |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Mean Diffusivity (MD)                         | Average diffusion rate across every axis (s/mm2)                        |
+       Tractoflow - DTI        +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Radial Diffusivity (RD)                       | Average diffusion rate across radial axes (s/mm2)                       |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Axial Diffusivity (AD)                        | Diffusion rate along the principal diffusion axis (s/mm2)               |
+-------------------------------+-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Fractional anisotropy tissue (FA-FWcorrected) |                                                                         |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Mean Diffusivity tissue (MD-FWcorrected)      |                                                                         |
+       Freewater Flow          +-----------------------------------------------+-------------------------------------------------------------------------+
|      DTI-FW corrected         | Radial Diffusivity tissue (RD-FWcorrected)    |                                                                         |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Axial Diffusivity tissue (AD-FWcorrected)     |                                                                         |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Free water (FW)                               | Estimation of the isotropic fraction                                    |
+-------------------------------+-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Total Apparent fiber density (AFD total)      | Spherical harmonic coefficient 0 of the fODF                            |
+      Tractoflow - FODF        +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Number of fober direction (NuFO)              | Number of local maxima of the fODF                                      |
+-------------------------------+-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Intra-cellular volume fraction (ICvf)         |                                                                         |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Extra-cellular volume fraction (ECvf)         |                                                                         |
+          NODDI Flow           +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Isotropic volume fraction (ISOvf)             | Estimates the volume fraction of extracellular free-water               |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | Orientation direction (OD)                    | Represents the orientational distribution of the intra-neurite space    |
+-------------------------------+-----------------------------------------------+-------------------------------------------------------------------------+
|                               | ihMT ratio (ihMTR)                            | Represent a measure of fractional myelin content                        |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | ihMT delta R1 saturation (ihMTsat)            |            				                                                      |
+          ihMT Flow            +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | MT ratio (MTR)                                |             				                                                    |
+                               +-----------------------------------------------+-------------------------------------------------------------------------+
|                               | MT saturation (MTsat)                         |            				                                                      |
+-------------------------------+-----------------------------------------------+-------------------------------------------------------------------------+

