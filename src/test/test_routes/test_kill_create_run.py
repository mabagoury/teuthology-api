# from main import app
# from services.helpers import get_token
# from test.conftest import mock_get_token
#
#
# def test_create_kill(test_client):
#     app.dependency_overrides[get_token] = mock_get_token
#     response = test_client.post(
#         "/kill",
#         headers={"Content-Type": "application/json"},
#         params={"dry_run": False, "logs": True},
#         json={
#             "--run": "run job",
#             "--preserve-queue": True,
#             "--job": ["job1", "job2"],
#             "--jobspec": "do job",
#             "--machine-type": "debian",
#             "--archive": "",
#             "--user": "vallariag",
#             "--dry-run": False,
#         },
#     )
#     assert response.status_code == 200
