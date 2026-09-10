from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


initial_activities = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(deepcopy(initial_activities))
    yield
    activities.clear()
    activities.update(deepcopy(initial_activities))


@pytest.fixture
def client():
    return TestClient(app)