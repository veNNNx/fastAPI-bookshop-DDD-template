import logging
import time

from pydantic_settings import BaseSettings, SettingsConfigDict


class LoggerSettings(BaseSettings):
    LOGFILE_PATHNAME: str = "central.log"
    LOG_FORMAT: str = (
        "%(asctime)s:%(name)s:%(funcName)s:%(lineno)d %(levelname)s %(message)s"
    )

    model_config = SettingsConfigDict(env_prefix="LOGGER_CONFIG_", case_sensitive=True)


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": LoggerSettings().LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "utc": {
            "()": UTCFormatter,
            "format": LoggerSettings().LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        # Debug file log handler saved to LOGFILE_PATHNAME, rotated daily at midnight
        "logfile": {
            "formatter": "utc",
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": LoggerSettings().LOGFILE_PATHNAME,
            "when": "midnight",
        },
        # Debug output handler
        "console": {
            "formatter": "utc",
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {"pymongo": {"level": "INFO"}, "pika": {"level": "ERROR"}},
    "root": {"level": "NOTSET", "handlers": ["logfile", "console"]},
}
