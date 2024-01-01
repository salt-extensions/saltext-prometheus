.. _user-documentation:

User Documentation
==================

Welcome to the Prometheus Salt Extension Documentation. This guide provides information on installing and using the Prometheus Salt Extension.


Introduction
------------

Prometheus Salt Extension is an extension of Salt that houses Prometheus related modules for easy plugin functionality.


Prometheus and Salt
~~~~~~~~~~~~~~~~~~~

The Prometheus tool is a widely-used open-source solution for monitoring and processing data. It provides a robust platform for real-time tracking of various system and application aspects.
In contrast, Salt is a powerful automation tool that offers flexible and scalable infrastructure management, streamlining tasks like configuration management and remote execution.

The Prometheus Salt extension helps integrate these tools by enhancing Salt's capabilities, catering specifically to Prometheus users' needs. This extension integrates seamlessly with Prometheus infrastructure, enabling effective monitoring and metrics gathering.


Modules
-------

The Prometheus Salt extension utilizes custom Salt modules to perform various functionalities.


Prometheus Textfile
~~~~~~~~~~~~~~~~~~~

Prometheus textfile module is a custom returner module.

    **What's a salt returner module?** A returner module defines the method and format in which the results of Salt execution commands are transmitted from the minions back to the master.


This module is used to output a `Text Exposition Format <https://prometheus.io/docs/instrumenting/exposition_formats/#text-format-example>`_ file on the minion. The output includes salt specific metrics gathered from the minion. The output is formatted to a file that can be ingested by Prometheus infrastructure for monitoring purposes.

To use the extension, you will need to provide a Salt state command and add a return flag pointed to the `prometheus_textfile` module. You can also utilize different configuration files to set the returner module.

Example usage command: ``salt \* state.apply test --return prometheus_textfile``

By default, the output file is located in the following file location: ``/var/cache/salt/minion/prometheus_textfile/salt.prom``, but this can be changed via a configuration file.

Note: The extension can be installed and used on all minions or specific minions where reporting data is needed

**Example output file:**

    .. code-block::

        salt_last_completed 1.698364953e+09
        # HELP salt_version Version of installed Salt package
        # TYPE salt_version gauge
        salt_version 3006.3
        # HELP salt_version_tagged Version of installed Salt package as a tag
        # TYPE salt_version_tagged gauge
        salt_version_tagged{salt_version="3006.3"} 1.0


Use Cases
*********

The Prometheus Salt Extension can be used to easily output Salt-specific metric data across systems using Salt. This data can be used in a variety of ways, including tracking minion states, Salt versions, and other Salt-specific metrics.

`Consider the following example:`

In a large environment where Salt is used for infrastructure management, Prometheus/Grafana infrastructure is installed with node-exporter running on the machines. An engineer installs the Prometheus Salt extension, enabling the generation of metrics data in a compatible format for node-exporter. Node-exporter transmits this data to the Prometheus infrastructure, where it becomes available for visualization in Grafana. Grafana serves as the visualization tool for these metrics and also includes an alerting system capable of identifying active minions and signaling failures within the system. This automated approach seamlessly integrates into both existing and new monitoring and alerting workflows within the Prometheus/Grafana ecosystem, facilitating the visualization and accessibility of information through established pipelines.

`Consider another example:`

A security vulnerability was found in the Salt version used on your minion machines. A patch was released, and your machines need to upgrade their Salt version to comply with security protocols. To facilitate this process, the Prometheus Salt Extension was integrated into your environment. The extension generated metric data that was incorporated into a Grafana dashboard within your current monitoring infrastructure, allowing you to track Salt versions across all minion machines.


Video Demo: `Nick the Salt Guy Demos the Prometheus Salt Extension <https://www.youtube.com/watch?v=8yv_AeHOHOE&t>`_


Installation
------------

Dependencies
~~~~~~~~~~~~

Before installing the Prometheus Salt extension, ensure you have the following
dependencies installed:

- Salt: Version 3005 or higher - If you don't have salt on your machine, visit salt installation guide here: `Salt Installation Guide <https://docs.saltproject.io/salt/install-guide/en/latest>`_

Several methods are available for installing this extension:

Method 1: Using pip
~~~~~~~~~~~~~~~~~~~

1. Open a terminal or command prompt.
2. Run the following command to install the Prometheus Salt extension:

  .. code-block:: bash

    pip install prometheus-salt

**IMPORTANT:** Depending on the version of Salt used, verify that the python you are using is the salt python most commonly found at **/opt/saltstack/salt/bin/python**

.. raw:: html

   <br />


Method 2: Using salt
~~~~~~~~~~~~~~~~~~~~
1. Verify salt is installed on the target machine
2. Run the following command to install the Prometheus Salt extension:

  .. code-block:: bash

    salt \* pip.install saltext-prometheus


`Once the extension is installed, you can verify the installation, or proceed to use the extension in your environment.`

**Verify Installation** - `(Optional)`

Verify that the extension is installed by running the following command:

.. code-block::

    salt --versions-report


You should see `saltext.prometheus` listed under Salt extensions.



**Using the Extension**

After successfully installing the extension, you are ready to execute Prometheus Salt extension modules.

.. raw:: html

   <br />

**Example:** Apply a test state using the prometheus_textfile as the returner

1. Create a test.sls file in the directory /srv/salt

**/srv/salt/test.sls**

.. code-block:: yaml

    /tmp/dummy.text:
        file.managed:
            - contents: |
                helloworld


2. Execute the following command:

.. code-block::

    salt \* state.apply test --return prometheus_textfile


3. Check the output file created on the minion machine (default location: **/var/cache/salt/minion/prometheus_textfile/salt.prom**).

**Example output file:**

    .. code-block::

        salt_last_completed 1.698364953e+09
        # HELP salt_version Version of installed Salt package
        # TYPE salt_version gauge
        salt_version 3006.3
        # HELP salt_version_tagged Version of installed Salt package as a tag
        # TYPE salt_version_tagged gauge
        salt_version_tagged{salt_version="3006.3"} 1.0


Configuration
-------------

The Prometheus Salt extension can be executed out-of-the-box with default settings. However, it offers configurable components that can be customized by modifying settings within a configuration file.

When adding a configuration file, the extension follows the same Salt convention for adding configurations. In the following example, we use the default location for Salt config files and the `prometheus_textfile` returner module.

In directory **/etc/salt/minion.d** we created a file called **prometheus.conf**

.. code-block::

  prometheus_textfile.filename: /prometheus/metrics/salt.prom

  return:
    - prometheus_textfile


`The example configuration sets the return to the prometheus_textfile and sets the prometheus_textfile location to a custom location.`


**Configurable Options**

Prometheus Textfile: See module documentation


Uninstall
---------

You can uninstall the Prometheus Salt Extension using pip:

.. code-block::

  pip uninstall prometheus-salt
