===
zca
===

ZCA whitening in python with a sklearn-like interface

Usage
-----

.. code:: python

    from zca import ZCA
    import numpy as np
    X = np.random.random((10000, 15)) # data array
    trf = ZCA().fit(X)
    X_whitened = trf.transform(X)
    X_reconstructed = trf.inverse_transform(X_whitened)
    assert(np.allclose(X, X_reconstructed)) # True


Installation
------------

.. code:: bash

    git clone https://github.com/mwv/zca.git
    cd zca; python setup.py install

Requirements
^^^^^^^^^^^^

- numpy
- scipy
- scikit-learn


Licence
-------
GPLv3

Authors
-------

`zca` was written by `Maarten Versteegh <maartenversteegh@gmail.com>`_.
