import eventlet
import socketio
from loguru import logger

from src.all_riddles import riddles

# Заставляем работать пути к статике
static_files = {'/': 'static/index.html', '/static': './static'}
sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files=static_files)

# Обрабатываем подключение пользователя
@sio.event
def connect(sid, environ):
    logger.info(f"Пользователь {sid} подключился")

# Обрабатываем запрос очерендного вопроса
@sio.on('next')
def next(sid, data):
   pass

# Обрабатывем отправку ответа
@sio.on('answer')
def receive_answer(sid, data):
    pass

# Обрабатываем отключение пользователя
@sio.event
def disconnect(sid):
     logger.info(f"Пользователь {sid} подключился")


eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 80)), app)
