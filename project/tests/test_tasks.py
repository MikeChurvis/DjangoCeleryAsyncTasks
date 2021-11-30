from unittest.mock import patch

from django.urls import reverse
from tasks import sample_tasks

def test_home(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200


def test_task():
    assert sample_tasks.create_task.run(1)
    assert sample_tasks.create_task.run(2)
    assert sample_tasks.create_task.run(3)

@patch("tasks.sample_tasks.create_task.run")
def test_mock_test(mock_run):
    assert sample_tasks.create_task.run(1)
    sample_tasks.create_task.run.assert_called_once_with(1)

    assert sample_tasks.create_task.run(2)
    assert sample_tasks.create_task.run.call_count == 2

    assert sample_tasks.create_task.run(3)
    assert sample_tasks.create_task.run.call_count == 3