# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
"""Unit test suite for ``base64io`` helpers."""
import sys

import pytest

import base64io

pytestmark = [pytest.mark.unit]


def test_py2():
    is_python2 = sys.version_info[0] == 2

    assert (is_python2 and base64io._py2()) or (not is_python2 and not base64io._py2())


def test_file():
    is_python2 = sys.version_info[0] == 2

    if is_python2:
        # If we are in Python 2, the "file" assignment should not
        # happen because it is a builtin object.
        assert not hasattr(base64io, "file")
    else:
        # If we are in Python 3, the "file" assignment should happen
        # to provide a concrete definition of the "file" name.
        assert base64io.file is NotImplemented


@pytest.mark.parametrize(
    "source, expected",
    (("asdf", b"asdf"), (b"\x00\x01\x02\x03", b"\x00\x01\x02\x03"), (u"\u1111\u2222", b"\xe1\x84\x91\xe2\x88\xa2")),
)
def test_to_bytes(source, expected):
    assert base64io._to_bytes(source) == expected
