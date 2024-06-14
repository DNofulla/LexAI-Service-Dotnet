from orchestrator_service.main import app

@app.get('/status')
def home():
    return 'Welcome to the LexAI Back End Service!'