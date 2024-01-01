Quick Start Guide
=================

This guide will show you how to get started running the Prometheus Salt extension.


Before You Start
----------------

Ensure Salt 3005 or above is installed and running on your machine.

If you haven't installed Salt yet, refer to the `Salt Installation Guide <https://docs.saltproject.io/salt/install-guide/en/latest>`_


Installing the Extension
------------------------

Several methods are available for installing the Prometheus Salt extension:

- **Method 1: Using pip**

.. code-block::

    pip install saltext-prometheus

.. note::
    Depending on the Salt version, Salt may not be using the system Python. For those versions, ensure you're using the Python associated with Salt (typically found at **/opt/saltstack/salt/bin/python**).


- **Method 2: Using Salt**

Use an execution module like:

.. code-block::

    salt \* pip.install saltext-prometheus


Note: The extension can be installed and used on all minions or specific minions where reporting data is needed


Verify Installation - (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Verify that the extension is installed

.. code-block::

    salt --versions-report

You should see `saltext.prometheus` listed under Salt extensions.


Getting Started
---------------

After successfully installing the extension, you are prepared to execute Prometheus Salt extension modules.

.. raw:: html

   <br />

**Example:** Apply a test state using the prometheus_textfile as the returner

Create a test.sls file in directory /srv/salt

/srv/salt/test.sls

.. code-block:: yaml

    /tmp/dummy.text:
        file.managed:
            - contents: |
                helloworld


Execute the following command

.. code-block::

    salt \* state.apply test --return prometheus_textfile


You should see an output file created on the minion machine (default location: **/var/cache/salt/minion/prometheus_textfile/salt.prom**).

**Example output file:**

    .. code-block::

        salt_last_completed 1.698364953e+09
        # HELP salt_version Version of installed Salt package
        # TYPE salt_version gauge
        salt_version 3006.3
        # HELP salt_version_tagged Version of installed Salt package as a tag
        # TYPE salt_version_tagged gauge
        salt_version_tagged{salt_version="3006.3"} 1.0


Additional Resources
--------------------

For more detailed information on functionality, use cases, and configuration, please vist our :ref:`user-documentation`
