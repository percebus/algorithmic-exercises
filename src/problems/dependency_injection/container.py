from lagom import Container

from problems.config.configuration import Configuration
from problems.config.os_environ.settings import Settings


def create_container() -> Container:
    container = Container()

    container[Settings] = Settings()
    container[Configuration] = lambda c: Configuration(settings=c[Settings])

    return container
