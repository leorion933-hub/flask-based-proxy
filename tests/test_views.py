# -*- coding: utf-8 -*-
"""API unit tests."""

import pytest
from flask import Flask
from api.extensions import cache
from unittest.mock import patch, MagicMock
from api.views import blueprint



@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(blueprint)
    app.config['TESTING'] = True
    app.config['CACHE_TYPE'] = 'SimpleCache'  # Use simple cache for testing
    cache.init_app(app)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Template-flask-app is Running" in resp.data

def test_cached_time(client):
    resp = client.get("/time")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "current_time" in data

def test_uncached_time(client):
    resp = client.get("/uncached-time")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "current_time" in data

@patch("api.views.create_task")
def test_run_task_with_time_param(mock_create_task, client):
    mock_task = MagicMock()
    mock_task.id = "fake-task-id"
    mock_create_task.delay.return_value = mock_task

    resp = client.get("/run-task?time=5")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["task_id"] == "fake-task-id"
    assert data["status"] == "Task submitted!"
    mock_create_task.delay.assert_called_with("5")

@patch("api.views.create_task")
def test_run_task_without_time_param(mock_create_task, client):
    mock_task = MagicMock()
    mock_task.id = "fake-task-id"
    mock_create_task.delay.return_value = mock_task

    resp = client.get("/run-task")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["task_id"] == "fake-task-id"
    assert data["status"] == "Task submitted!"
    mock_create_task.delay.assert_called_with(10)