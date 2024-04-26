import uvicorn
from pawapi.router import app

uvicorn.run(app, host="localhost", port=8080)
