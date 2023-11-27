from fastapi.testclient import TestClient
from chatroom_project.main import app


client = TestClient(app)

def test_create_chatroom():
    response = client.post("/chatroom/1")
    assert response.status_code == 200 #404
    assert response.json() == {"chatroom_id": "1 successfully created"}
