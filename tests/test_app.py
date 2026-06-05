def test_root_redirects_to_static_index(test_client):
    # Arrange
    url = "/"

    # Act
    response = test_client.get(url, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_activity_list(test_client):
    # Arrange
    url = "/activities"

    # Act
    response = test_client.get(url)

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"], dict)
    assert data["Chess Club"]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
