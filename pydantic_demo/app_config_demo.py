import logging
from pydantic import BaseSettings


class LoggingSettings(BaseSettings):

    LOGGING_LEVEL: int = logging.INFO


class DBSettings(BaseSettings):

    SQLALCHEMY_DATABASE_URI: str = ''


class AppSettings(BaseSettings):

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    logging: LoggingSettings = LoggingSettings()
    db: DBSettings = DBSettings()



if __name__ == '__main__':
    setting = AppSettings()
    import ipdb; ipdb.set_trace()
    print(setting)

