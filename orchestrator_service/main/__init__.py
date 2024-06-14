from flask import Flask

app = Flask(__name__)

from orchestrator_service.routes import test