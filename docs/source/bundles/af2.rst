Test full AF and tab plots
==========================

.. figure:: ../_static/AF/AF.gif
    :align: center
    :figwidth: 60%

    Arcuate Fasciculus - Appears in the following order: local coloring, uniform coloring, profile coloring


Heatmap with frame
------------------------

Association between different MRI measures extracted from AF are evaluated using Pearson's correlation coefficient (r) and evaluated for each session (slider). For better contrast, Pearson correlation coefficients are displayed as absolute values.

.. raw:: html frame

    <iframe src="../_static/AF_correlation_map_with_slider.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


Correlations without frame
------------------------

Here we use a scatterplot with a trend line to provide more information about the relationship between MRI measurements. Ordinary least squares (OLS) is used to evaluate the linear regression. OLS information is provided as a legend for each pair of measurements extracted from the AF. Use the menu to change the pair of associations.


.. raw:: html

    <iframe src="../_static/AF/AF_correlation_plots.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


Whole-Bundle Measures
------------------------

The figures below show the distribution of each measurement for all sessions. 
Use the slider to change the MRI measurements.
For ease of reading, RD, MD and AD values are expressed in x10-3 and ihMTsat values are expressed in x10-1.


.. raw:: html 

    <iframe src="../_static/AF/AF_boxplot_measures.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


Volume by sections
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <iframe src="../_static/AF/AF_volume_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


DTI measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html

    <iframe src="../_static/AF/DTI__AF_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


DTI-FW measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html

    <iframe src="../_static/AF/DTI-FW__AF_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

FW measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html

    <iframe src="../_static/AF/FW__AF_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

FODF measures
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    <iframe src="../_static/AF/FODF__AF_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

NODDI measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html

    <iframe src="../_static/AF/NODDI__AF_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


MTI measures
~~~~~~~~~~~~~~~~~~~~~~~


.. raw:: html

    <iframe src="../_static/AF/MTI__AF_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


Statistic descriptives
------------------------


This section provides descriptive statistics for IRM metrics averaged
over all streamlines and bundle-specific metrics.


.. tabs::

   .. tab:: Average

      .. tabs::

         .. tab:: Streamlines

            .. csv-table:: Streamlines stats
              :file: ../_static/AF/AF_streamlines_summary.csv
              :header-rows: 1

         .. tab:: Measures

            .. csv-table:: MRI measurements
              :file: ../_static/AF/AF_average_summary.csv
              :header-rows: 1

   .. tab:: Profiles

      .. tabs::

         .. tab:: Volume

            .. csv-table:: Volume by section
              :file: ../_static/AF/AF__profile_volume_summary.csv
              :header-rows: 1

         .. tab:: DTI

            .. csv-table:: Measures by section
              :file: ../_static/AF/DTI__profile_summary.csv
              :header-rows: 1

         .. tab:: DTI-FW

            .. csv-table:: Measures by section
              :file: ../_static/AF/DTI-FW__profile_summary.csv
              :header-rows: 1

         .. tab:: FW

            .. csv-table:: Measures by section
              :file: ../_static/AF/FW__profile_summary.csv
              :header-rows: 1

         .. tab:: FODF

            .. csv-table:: Measures by section
              :file: ../_static/AF/FODF__profile_summary.csv
              :header-rows: 1

         .. tab:: NODDI

            .. csv-table:: Measures by section
              :file: ../_static/AF/NODDI__profile_summary.csv
              :header-rows: 1

         .. tab:: MTI

            .. csv-table:: Measures by section
              :file: ../_static/AF/MTI__profile_summary.csv
              :header-rows: 1

         .. tab:: Plots MTI test

            .. raw:: html

                <iframe src="../_static/AF/MTI__AF_profile.html"  width=800 height=500 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>
