from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DB_NAME = "test_postgres"
TEST_DATABASE_URL = f"postgresql://root:password@localhost:5432/{TEST_DB_NAME}"

engine = create_engine(TEST_DATABASE_URL)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
