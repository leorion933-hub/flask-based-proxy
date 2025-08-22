# -*- coding: utf-8 -*-
"""Views section."""

import time
from api.extensions import cache
from api.tasks import create_task
from flask import (
    Blueprint,
    request,
    jsonify,
)

blueprint = Blueprint("public", __name__)


@blueprint.route("/time")
@cache.cached(timeout=20)
def cached_time():
    return jsonify({
        "current_time": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@blueprint.route("/uncached-time")
def uncached_time():
    return jsonify({
        "current_time": time.strftime("%Y-%m-%d %H:%M:%S")
    })

@blueprint.route("/", methods=["GET"])
def index():
    return "Template-flask-app is Running"

@blueprint.route("/run-task", methods=["GET"])
def run_task():
    query = request.args.get("time")
    if not query:
        query = 10

    task = create_task.delay(query)
    return jsonify({"task_id": task.id, "status": "Task submitted!"})
