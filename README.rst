SCIL multimodal MRI longitudinal database
==========================================

The SCIL longitudinal multimodal MRI database is a single-center, repeated-measures study that collects
multimodal MRI data with a high number of acquisitions over a short period of time in healthy subjects.
This dataset includes :
    * anatomical image (3DT1)
    * multi-shell diffusion weighted images (DWI)
    * inhomogeneous MT images (ihMT - MTI)


Ce site fournit une description des valeurs moyennes pour les mesures
IRMs qui peuvent etre generes par les outils developed by the Sherbrooke Connectivity Imaging Lab (`SCIL`_)

 .. _SCIL: http://scil.dinf.usherbrooke.ca/


SCIL tools
-----------------

The SCIL tools is open-source here: `scilpy <https://github.com/scilus/scilpy>`__. 
Full documentation, including installation, a description of the scilpy tools and pipelines can be found `here <https://scil-documentation.readthedocs.io/>`__.


Tools used for images processing are listed below and available on `SCIL <https://github.com/scilus>`__ :

   - Tractoflow : https://github.com/scilus/tractoflow
   - NODDI flow : https://github.com/scilus/noddi_flow
   - Freewater flow : https://github.com/scilus/freewater_flow
   - ihMT flow : https://github.com/scilus/ihmt_flow
   - DMRIqc flow : https://github.com/scilus/dmriqc_flow
   - RBX flow : https://github.com/scilus/rbx_flow
   - Tractometry flow : https://github.com/scilus/tractometry_flow


Publications
-----------------

A description of the variability and consistency of MRI measurements over time has been published:

Edde M., Theaud G., [...] and Descoteaux M.
High-frequency longitudinal white matter diffusion- & myelin-based MRI database: 
reliability and variability, currently. https://onlinelibrary.wiley.com/doi/10.1002/hbm.26310

:download:`PDF<./download/Edde2023_HBM_HighFrequencyLongitudinal.pdf>`

Results of consistency analyzes could also be find here :
https://high-frequency-mri-database-supplementary.rtfd.io




.. toctree::
   :maxdepth: 1
   :caption: Data

   data/data_description

.. toctree::
   :maxdepth: 1
   :caption: Pipeline

   pipeline/mri_processing
   pipeline/bundles

.. toctree::
   :maxdepth: 1
   :caption: Results

   results/average_maps
   results/correlation
   results/measure

.. toctree::
   :maxdepth: 1
   :caption: Download

   download/download_data

