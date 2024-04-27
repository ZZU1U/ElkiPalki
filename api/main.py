import sys
sys.dont_write_bytecode = True # Disables pycache

import uvicorn
from pawapi.router import app

uvicorn.run(app, host="localhost", port=8080)

# Типы кормой для собак
# Отменить бронь
# Для собак выбирать периоды
