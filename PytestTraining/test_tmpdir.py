import pytest

tmpdir = local('PYTEST_TMPDIR/test_needsfiles0')
class test_needfiles(tmpdir):
    print(tmpdir)
    assert 0
