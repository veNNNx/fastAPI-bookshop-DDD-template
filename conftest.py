import pytest
from dependency_injector import providers
from sqlalchemy import create_engine, text

from backend.books import BookTable
from backend.common import DATABASE_URL, TEST_DB_NAME, Base
from backend.common.postgres_test import TestingSessionLocal, engine
from backend.ioc_container import ApplicationContainer


def override_dbs(container: ApplicationContainer) -> ApplicationContainer:
    container.books.book_tabel.override(
        providers.Factory(BookTable, session=TestingSessionLocal)
    )

    return container


def create_test_database():
    admin_engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")
    with admin_engine.connect() as conn:
        exists = conn.execute(
            text(f"SELECT 1 FROM pg_database WHERE datname = '{TEST_DB_NAME}'")
        ).scalar()
        if not exists:
            conn.execute(text(f"CREATE DATABASE {TEST_DB_NAME}"))
            print("Created database:", TEST_DB_NAME)


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    create_test_database()

    Base.metadata.create_all(bind=engine)
    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def test_app_container():
    container = ApplicationContainer()
    container.init_resources()
    container.wire(packages=["api", "backend"])

    container = override_dbs(container)

    Base.metadata.create_all(bind=engine)
    yield container
    Base.metadata.drop_all(bind=engine)

    container.shutdown_resources()
    container.books.book_tabel.reset_override()
