Arcuate Fasciculus
==========================

.. figure:: ../_static/Bundles/AF/AF.gif
    :align: center
    :figwidth: 55%

    **Arcuate Fasciculus** - Appears in the following order: local coloring, uniform coloring, profile coloring.


Heatmap
------------------------

Association between different MRI measures extracted from AF are evaluated using 
Pearson's correlation coefficient (r) and evaluated for each session  and session average (mean). 
Use the slider to change the session and mean.
For better contrast, Pearson correlation coefficients are displayed as absolute values.

.. raw:: html

    <iframe src="../_static/Bundles/AF/AF_correlation_map_with_slider.html"  width=800 height=800 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


Correlations - OLS regression
-------------------------------

We use a scatter plot with a trend line to provide more information on the 
relationship between MRI measurements using the **mean value over all sessions** (not per session). 
Ordinary least squares (OLS) is used to evaluate the linear regression. 
OLS information is provided as a legend for each pair of measurements extracted from the bundle. 
Use the menu to change the pair of associations.


.. raw:: html

    <iframe src="../_static/Bundles/AF/AF_correlation_plots.html"  width=1000 height=800 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


Bundle average Streamlines
------------------------

The figures below show the distribution of each streamline measures for all sessions and session average.
Use the slider to change the streamlines measures.


.. raw:: html

    <iframe src="../_static/Bundles/AF/AF_boxplot_volume.html"  width=950 height=700 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>



Bundle average measures
------------------------

The figures below show the distribution of each measurement for all sessions and session average.
Use the slider to change the MRI measurements. 
For ease of reading, RD, MD and AD values are expressed in x10-3 s/mm2 and ihMTsat values are expressed in x10-1.


.. raw:: html 

    <iframe src="../_static/Bundles/AF/AF_boxplot_measures.html"  width=950 height=700 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>


Bundle-Profile
------------------------

The tabs below show the bundle profiles for all sessions and session average (mean). 
Use the slider to change the session and mean. 
For ease of reading, RD, MD and AD values are expressed in x10-3 and ihMTsat values in x10-1.


.. tabs::

   .. tab:: Profiles

      .. tabs::

         .. tab:: Volume

            .. raw:: html

                <iframe src="../_static/Bundles/AF/AF_Streamlines__profile.html"  width=600 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

         .. tab:: DTI

            .. raw:: html

                <iframe src="../_static/Bundles/AF/AF_DTI__profile.html"  width=600 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

         .. tab:: DTI-FW - test resize

            .. raw:: html

                <iframe src="../_static/Bundles/AF/AF_DTI-FW__profile.html"  width=600 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

         .. tab:: FW - resize smaller

            .. raw:: html

                <iframe src="../_static/Bundles/AF/AF_FW__profile.html"  width=600 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

         .. tab:: FODF

            .. raw:: html

                <iframe src="../_static/Bundles/AF/AF_FODF__profile.html"  width=600 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

         .. tab:: NODDI

            .. raw:: html

                <iframe src="../_static/Bundles/AF/AF_NODDI__profile.html"  width=600 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>

         .. tab:: MTI

            .. raw:: html

                <iframe src="../_static/Bundles/AF/AF_MTI__profile.html"  width=600 height=400 style="padding:0; border:0; display: block; margin-left: auto; margin-right: auto"></iframe>



Statistic descriptive
------------------------

This section provides descriptive statistics for all measures extracted 
for bundle-streamlines, bundle-average and bundle-profile.


.. tabs::

   .. tab:: Average

      .. tabs::

         .. tab:: Streamlines

            .. csv-table:: Bundle streamlines
              :file: ../_static/Bundles/AF/AF_streamlines_summary.csv
              :header-rows: 1

         .. tab:: Measures

            .. csv-table:: Measures
              :file: ../_static/Bundles/AF/AF_average_summary.csv
              :header-rows: 1

   .. tab:: Profiles

      .. tabs::

         .. tab:: Volume

            .. csv-table:: Volume by section
              :file: ../_static/Bundles/AF/AF__profile_volume_summary.csv
              :header-rows: 1

         .. tab:: DTI

            .. csv-table:: DTI by section
              :file: ../_static/Bundles/AF/DTI__profile_summary.csv
              :header-rows: 1

         .. tab:: DTI-FW

            .. csv-table:: DTI-FW by section
              :file: ../_static/Bundles/AF/DTI-FW__profile_summary.csv
              :header-rows: 1

         .. tab:: FW

            .. csv-table:: FW by section
              :file: ../_static/Bundles/AF/FW__profile_summary.csv
              :header-rows: 1

         .. tab:: FODF

            .. csv-table:: FODF by section
              :file: ../_static/Bundles/AF/FODF__profile_summary.csv
              :header-rows: 1

         .. tab:: NODDI

            .. csv-table:: NODDI by section
              :file: ../_static/Bundles/AF/NODDI__profile_summary.csv
              :header-rows: 1

         .. tab:: MTI

            .. csv-table:: MTI by section
              :file: ../_static/Bundles/AF/MTI__profile_summary.csv
              :header-rows: 1
