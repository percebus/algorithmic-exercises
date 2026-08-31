import json
import logging
import logging.config
from dataclasses import dataclass, field
from logging import Logger
from typing import Any

from problems.config.os_environ.settings import Settings


@dataclass
class Configuration:
    settings: Settings = field(default_factory=Settings)

    # pylint: disable=W0108 # unnecessary-lambda
    logging: dict[str, Any] = field(init=False)
    # pylint: enable=W0108

    logger: Logger = field(init=False)

    def configure_logging(self) -> None:
        _path: str = self.settings.logging_config or ""

        with open(_path, "r", encoding="utf-8") as f:
            logging_config = json.load(f)

        logging.config.dictConfig(logging_config)
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Configuration: initializing...")

    def __post_init__(self) -> None:
        self.configure_logging()
