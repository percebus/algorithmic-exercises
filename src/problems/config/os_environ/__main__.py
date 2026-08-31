from dotenv import load_dotenv
from lagom import Container

from problems.commons.printing import pprint
from problems.config.os_environ.settings import Settings
from problems.dependency_injection.container import create_container


def run(container: Container) -> None:
    settings = container[Settings]
    pprint(settings.safe_model_dump())


def main() -> None:
    load_dotenv()
    container: Container = create_container()
    run(container)


if __name__ == "__main__":
    main()
