import pytest

@pytest.fixture(autouse=True)
def base_url():
    """All summaries and owners are unique."""
    return 'https://reqres.in/api'

@pytest.fixture
def supply_url():
    return "https://reqres.in/api"