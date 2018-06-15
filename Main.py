import logging
from GUI_Main import start_application


if __name__ == "__main__":
    logging.basicConfig(filename='logger_errors/myexample.log', level=logging.DEBUG)
    start_application()
