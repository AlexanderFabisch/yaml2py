.. yaml2py documentation master file, created by
   sphinx-quickstart on Tue Nov  4 22:30:13 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

yaml2py
=======

yaml2py allows you to automatically generate Python objects from YAML
configuration files or Python dictionaries.

Example
-------

For example, consider you have discovered an awesome setup to solve your
machine learning problem with scikit-learn. You can write it down as a YAML
file and mail it to a friend.

.. code-block:: yaml

    type: sklearn.pipeline.Pipeline
    steps:
        - - pca
          - package: sklearn.decomposition
            type: PCA
            n_components: 50
        - - svc
          - type: sklearn.svm.SVC
            gamma: 10.0

Note that you only have to add the entries for package and type besides the
regular constructor arguments. Loading the Python object is simple:

.. code-block:: python

    import yaml2py
    pipeline = yaml2py.from_yaml("config.yaml")

Note that yaml2py will recursively convert dictionaries to Python objects. That
is why it will not only generate a pipeline object but also a PCA object and an
SVC object that will be passed to the pipeline constructor.
