########
base64io
########

.. image:: https://img.shields.io/pypi/v/base64io.svg
   :target: https://pypi.python.org/pypi/base64io
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/base64io.svg
   :target: https://pypi.python.org/pypi/base64io
   :alt: Supported Python Versions

.. image:: https://readthedocs.org/projects/base64io-python/badge/
   :target: https://base64io-python.readthedocs.io/en/stable/
   :alt: Documentation Status

Python has had native base64 encoding support since 2.4, which is great. However, when we
needed to encoded and decode streaming data, we realized that there is no streaming interface
for base64 encoding, and there doesn't appear to be anything available from the community
either.

There is the legacy ``base64.encode`` and ``base64.decode`` interface, but while this interface
lets you shuffle data between two streams, it assumes that you are starting with two complete
streams. What we really wanted was a standard stream that applies base64 encoding/decoding.

This led us to build :class:`base64io.Base64IO`.

The latest full documentation can be found at `Read the Docs`_.

Find us on `GitHub`_.

***************
Getting Started
***************

:class:`base64io.Base64IO` has no dependencies outside of the standard library and should
work with any version of Python after 2.6. We test it for 2.6, 2.7, 3.3, 3.4, 3.5, 3.6, and
3.7.

Installation
============

.. code::

   $ pip install base64io

***
Use
***
:class:`base64io.Base64IO` works by wrapping another stream and transparently transforming
data written to or read from that stream.

* ``write()`` encodes data before writing it to the wrapped stream
* ``read()`` decodes data after reading it from the wrapped stream

Because the position of the :class:`base64io.Base64IO` stream and the wrapped stream will
almost always be differently, :class:`base64io.Base64IO` does not support:

* ``seek()``
* ``tell()``

:class:`base64io.Base64IO` also does not support:

* ``fileno()``
* ``truncate()``

Encode data
===========

.. warning::

   Any time you are writing to a :class:`base64io.Base64IO` stream, you **must** close the
   stream after your final write. Because of how the base64 transformation works, up to two
   bytes of unencoded data might be held in an internal buffer and not written to the wrapped
   stream. Calling ``close()`` flushes this buffer and writes the padded result to the wrapped
   stream.

   If you are using :class:`base64io.Base64IO` as a context manager, we take care of this for you.

.. code-block:: python

   from base64io import Base64IO

   with open('source_file', 'rb') as source, open('encoded_file', 'wb') as target:
      with Base64IO(target) as encoded_target:
         for line in source:
            encoded_target.write(line)

Decode data
===========

.. note::

   Because of how the base64 transformation works, any calls to ``read()`` might read up
   to three additional bytes from the underlying stream.

.. code-block:: python

   from base64io import Base64IO

   with open('encoded_file', 'rb') as encoded_source, open('target_file', 'wb') as target:
      with Base64IO(encoded_source) as source:
         for line in source:
            target.write(line)

*******
License
*******

This library is licensed under the Apache 2.0 License.

.. _Read the Docs: http://base64io-python.readthedocs.io/en/latest/
.. _GitHub: https://github.com/awslabs/base64io-python/
.. _base64 documentation: https://docs.python.org/3/library/base64.html#base64.decode
