"""Base64IO stream handler."""
import io
import os
import re

from setuptools import find_packages, setup

VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*args):
    """Read complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


def readme():
    """Read and patch README."""
    readme_text = read("README.rst")
    # PyPI does not accept :class: references.
    return readme_text.replace(":class:`base64io.Base64IO`", "``base64io.Base64IO``")


def get_version():
    """Read the version from this module."""
    init = read("src", "base64io", "__init__.py")
    return VERSION_RE.search(init).group(1)


setup(
    name="base64io",
    version=get_version(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/aws/base64io-python",
    author="Amazon Web Services",
    author_email="aws-cryptools@amazon.com",
    maintainer="Amazon Web Services",
    long_description=readme(),
    keywords="base64 stream",
    data_files=["README.rst", "CHANGELOG.rst", "LICENSE"],
    license="Apache License 2.0",
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
