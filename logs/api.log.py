import logging


# логгеры
logger_api = logging.getLogger('one')

# обработчик логгера
logger_handler = logging.StreamHandler()

# форматирование(Formatter)
formatter_one = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
logger_handler.setFormatter(formatter_one)

# к журналу
logger_api.addHandler(logger_handler)
# запись логов
logging.basicConfig(filename="logs/api.log", level=logging.DEBUG)
