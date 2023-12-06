Arcuate Fasciculus
==========================

.. figure:: ../data/AF/AF.gif
    :align: center
    :figwidth: 60%

    Arcuate Fasciculus - Appears in the following order: local coloring, uniform coloring, profile coloring


Heatmap
------------------------

Association between different MRI measures extracted from AF are evaluated using Pearson's correlation coefficient (r) and evaluated for each session (slider). For better contrast, Pearson correlation coefficients are displayed as absolute values.


.. raw:: html
  :file: ../data/AF/AF_correlation_map_with_slider.html


Correlations
------------------------

Here we use a scatterplot with a trend line to provide more information about the relationship between MRI measurements. Ordinary least squares (OLS) is used to evaluate the linear regression. OLS information is provided as a legend for each pair of measurements extracted from the AF. Use the menu to change the pair of associations.


.. raw:: html
  :file: ../data/AF/AF_correlation_plots.html


Whole-Bundle Measures
------------------------

The figures below show the distribution of each measurement for all sessions. 
Use the slider to change the MRI measurements.
For ease of reading, RD, MD and AD values are expressed in x10-3 and ihMTsat values are expressed in x10-1.


.. raw:: html
  :file: ../data/AF/AF_boxplot_measures.html


Volume by sections
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html
  :file: ../data/AF/AF_volume_profile.html


DTI measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html
  :file: ../data/AF/DTI__AF_profile.html


DTI-FW measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html
  :file: ../data/AF/DTI-FW__AF_profile.html


FW measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html
  :file: ../data/AF/FW__AF_profile.html


FODF measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html
  :file: ../data/AF/FODF__AF_profile.html


NODDI measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html
  :file: ../data/AF/NODDI__AF_profile.html


MTI measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html
  :file: ../data/AF/MTI__AF_profile.html


Stats desc
------------------------

This section provides descriptive statistics for IRM metrics averaged
over all streamlines and bundle-specific metrics.


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
