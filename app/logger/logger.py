import logging

log_path = "app\logger\logs\custom.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logger level


# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)


file_handler = logging.FileHandler(log_path, mode="a", encoding="utf-8")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M"
)


# console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


if not logger.handlers:
    # logger.addHandler(console_handler)
    logger.addHandler(file_handler)


# logger.warning("This is a warning message")
# logger.info("This is an info message")
