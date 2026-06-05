import uuid


def test_signup_for_activity_adds_participant(test_client):
    # Arrange
    activity_name = "Chess Club"
    email = f"student+{uuid.uuid4().hex}@mergington.edu"
    signup_url = f"/activities/{activity_name}/signup"
    activity_url = "/activities"

    # Act
    signup_response = test_client.post(signup_url, params={"email": email})
    activities_response = test_client.get(activity_url)
    participants = activities_response.json()[activity_name]["participants"]

    # Assert
    assert signup_response.status_code == 200
    assert signup_response.json()["message"] == f"Signed up {email} for {activity_name}"
    assert email in participants


def test_signup_duplicate_participant_returns_400(test_client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    signup_url = f"/activities/{activity_name}/signup"

    # Act
    response = test_client.post(signup_url, params={"email": email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already registered for this activity"


def test_signup_for_unknown_activity_returns_404(test_client):
    # Arrange
    signup_url = "/activities/Unknown Club/signup"
    email = "test@mergington.edu"

    # Act
    response = test_client.post(signup_url, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_participant_from_activity(test_client):
    # Arrange
    activity_name = "Swimming Club"
    email = f"student+{uuid.uuid4().hex}@mergington.edu"
    signup_url = f"/activities/{activity_name}/signup"
    remove_url = f"/activities/{activity_name}/participant"

    # Act
    signup_response = test_client.post(signup_url, params={"email": email})
    remove_response = test_client.delete(remove_url, params={"email": email})

    # Assert
    assert signup_response.status_code == 200
    assert remove_response.status_code == 200
    assert remove_response.json()["message"] == f"Removed {email} from {activity_name}"


def test_remove_unknown_participant_returns_404(test_client):
    # Arrange
    activity_name = "Swimming Club"
    email = "nonexistent@mergington.edu"
    remove_url = f"/activities/{activity_name}/participant"

    # Act
    response = test_client.delete(remove_url, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"


def test_remove_participant_from_unknown_activity_returns_404(test_client):
    # Arrange
    remove_url = "/activities/Unknown Club/participant"
    email = "test@mergington.edu"

    # Act
    response = test_client.delete(remove_url, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
