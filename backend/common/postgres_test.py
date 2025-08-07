from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "postgresql://root:password@localhost:5432/test_postgres"

test_engine = create_engine(TEST_DATABASE_URL, isolation_level="AUTOCOMMIT")


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
)
