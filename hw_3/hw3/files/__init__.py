import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


BOOKS_CSV = get_path(filename="books.csv")
USER_JSON = get_path(filename="user.json")
REFERENCE_JSON = get_path(filename="reference.json")
RESULT_JSON = get_path(filename="result.json")
