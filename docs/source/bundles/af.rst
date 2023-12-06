Arcuate Fasciculus
==========================

.. figure:: ../data/AF/AF.gif
    :align: center
    :figwidth: 60%

    Arcuate Fasciculus - Appears in the following order: local coloring, uniform coloring, profile coloring


Statistics descriptive
-------------------------------

This section provides descriptive statistics for IRM metrics averaged
over all streamlines and bundle-specific metrics.

.. tabs::

    .. tab:: Bundle

        .. csv-table:: Statistics descriptive of Streamlines measures
           :file: ../data/AF/AF_streamlines_summary.csv
           :header-rows: 1


    .. tab:: Measure

        .. csv-table:: Statistics descriptive of bundle measures
           :file: ../data/AF/AF_average_summary.csv
           :header-rows: 1


Statistics Test copy tabs from rtd - why not working ?
-------------------------------------------

This section provides descriptive statistics for IRM metrics averaged
over all streamlines and bundle-specific metrics.

.. tabs::

    .. tab:: Sphinx

        If your project uses Sphinx,
        we offer a special builder optimized for Sphinx projects.


    .. tab:: MkDocs

        If your project uses MkDocs,
        we offer a special builder optimized for MkDocs projects.


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


Profile-Bundle Measures
------------------------

Statistics by sections
~~~~~~~~~~~~~~~~~~~~~~~


.. csv-table:: Statistics descriptive of profile bundle
    :file: ../data/AF/AF_profile_summary.csv
    :header-rows: 1
    :class: longtable
    :widths: 1 1


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


Profile Measures - Tabs version
---------------------------------

Here configuration with tab.

.. tabs::

    .. tab:: Volume

        .. raw:: html
          :file: ../data/AF/AF_volume_profile.html


    .. tab:: DTI

        .. raw:: html
          :file: ../data/AF/DTI__AF_profile.html


    .. tab:: DTI-FW

        .. raw:: html
          :file: ../data/AF/DTI-FW__AF_profile.html


    .. tab:: FW

        .. raw:: html
          :file: ../data/AF/FW__AF_profile.html


    .. tab:: FODF

        .. raw:: html
          :file: ../data/AF/FODF__AF_profile.html


    .. tab:: NODDI

        .. raw:: html
          :file: ../data/AF/NODDI__AF_profile.html


    .. tab:: MTI

        .. raw:: html
          :file: ../data/AF/MTI__AF_profile.html
