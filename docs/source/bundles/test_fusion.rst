Statistic descriptives
==========================


This section provides descriptive statistics for IRM metrics averaged
over all streamlines and bundle-specific metrics.

AF
------------------------


.. tabs::

   .. tab:: Average

      .. tabs::

         .. tab:: Streamlines

            .. csv-table:: Streamlines stats
              :file: ../data/AF/AF_streamlines_summary.csv
              :header-rows: 1

         .. tab:: Measures

            .. csv-table:: MRI measurements
              :file: ../data/AF/AF_average_summary.csv
              :header-rows: 1

   .. tab:: Profiles

      .. tabs::

         .. tab:: Volume

            .. csv-table:: Volume by section
              :file: ../data/AF/AF__profile_volume_summary.csv
              :header-rows: 1

         .. tab:: DTI

            .. csv-table:: Measures by section
              :file: ../data/AF/DTI__profile_summary.csv
              :header-rows: 1

         .. tab:: DTI-FW

            .. csv-table:: Measures by section
              :file: ../data/AF/DTI-FW__profile_summary.csv
              :header-rows: 1

         .. tab:: FW

            .. csv-table:: Measures by section
              :file: ../data/AF/FW__profile_summary.csv
              :header-rows: 1

         .. tab:: FODF

            .. csv-table:: Measures by section
              :file: ../data/AF/FODF__profile_summary.csv
              :header-rows: 1

         .. tab:: NODDI

            .. csv-table:: Measures by section
              :file: ../data/AF/NODDI__profile_summary.csv
              :header-rows: 1

         .. tab:: MTI

            .. csv-table:: Measures by section
              :file: ../data/AF/MTI__profile_summary.csv
              :header-rows: 1

         .. tab:: Plots


            .. raw:: html
              :file: ../data/AF/DTI__AF_profile.html


Heatmap
------------------------

Association between different MRI measures extracted from AF are evaluated using Pearson's correlation coefficient (r) and evaluated for each session (slider). For better contrast, Pearson correlation coefficients are displayed as absolute values.


.. raw:: html
  :file: ../data/AF/AF_correlation_map_with_slider.html

  