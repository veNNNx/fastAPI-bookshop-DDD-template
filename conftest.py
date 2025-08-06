import pytest
from dependency_injector import providers
from fastapi.testclient import TestClient
from sqlalchemy import text

from api.api.app_factory import create_app
from backend.common import Base, Tables, TestingSessionLocal, engine, test_engine
from backend.ioc_container import ApplicationContainer


def create_test_database():
    with engine.connect() as conn:
        exists = conn.execute(
            text("SELECT 1 FROM pg_database WHERE datname = 'test_postgres'")
        ).scalar()
        if not exists:
            conn.execute(text("CREATE DATABASE test_postgres"))
            print("✅ Created test database: test_postgres")


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    create_test_database()
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="session")
def test_app_container():
    container = ApplicationContainer()
    container.init_resources()
    container.wire(packages=["api", "backend"])

    container.session_factory.override(providers.Singleton(lambda: TestingSessionLocal))

    yield container

    container.shutdown_resources()
    container.session_factory.reset_override()


@pytest.fixture(scope="session")
def client(test_app_container: ApplicationContainer) -> TestClient:
    test_app = create_app(test_app_container)
    return TestClient(test_app)


@pytest.fixture(autouse=True)
def clean_db_after_test():
    yield
    with test_engine.connect() as conn:
        tables = ", ".join(table.value for table in Tables)
        conn.execute(text(f"TRUNCATE TABLE {tables} RESTART IDENTITY CASCADE"))
        conn.commit()
