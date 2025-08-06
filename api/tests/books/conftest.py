# from fastapi.testclient import TestClient
# from pytest import fixture

# from api.tests.books.steps import Steps
# from backend.ioc_container import ApplicationContainer


# @fixture
# def steps(container: ApplicationContainer, test_app: TestClient) -> Steps:
#     return Steps(books_service=container.books_service(), test_app=test_app)
