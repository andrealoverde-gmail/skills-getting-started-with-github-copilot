from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_delete_signup_removes_participant():
    activity_name = "Chess Club"
    email = "student@example.com"

    activities[activity_name]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]

    response = client.delete(f"/activities/{activity_name}/signup?email={email}")

    assert response.status_code == 404

    response = client.delete(f"/activities/{activity_name}/signup?email=michael@mergington.edu")

    assert response.status_code == 200
    assert "michael@mergington.edu" not in activities[activity_name]["participants"]


def test_delete_signup_rejects_unknown_participant():
    activity_name = "Chess Club"
    activities[activity_name]["participants"] = ["michael@mergington.edu"]

    response = client.delete(f"/activities/{activity_name}/signup?email=missing@example.com")

    assert response.status_code == 404
