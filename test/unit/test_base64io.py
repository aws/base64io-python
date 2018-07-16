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
    is_2 = sys.version_info[0] == 2

    assert (is_2 and base64io._py2()) or (not is_2 and not base64io._py2())


def test_file():
    is_2 = sys.version_info[0] == 2

    if is_2:
        assert not hasattr(base64io, 'file')
    else:
        assert base64io.file is NotImplemented
