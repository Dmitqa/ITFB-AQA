import csv
import json
from itertools import cycle
from files import BOOKS_CSV, USER_JSON, RESULT_JSON
from model_pydantic import Books, Reference

with (open(BOOKS_CSV, "r") as books,
      open(USER_JSON, "r") as user,
      open(RESULT_JSON, "w") as result):
    new_books = list(csv.DictReader(books))
    mod_books = [Books(title=row["Title"], author=row["Author"], pages=row["Pages"], genre=row["Genre"]).model_dump()
                 for row in new_books]

    new_user = json.load(user)
    mod_user = [Reference(**i).model_dump() for i in new_user]

    cycle_iter = cycle(mod_user)

    for book in mod_books:
        next(cycle_iter)["books"].append(book)

    json.dump(mod_user, result, indent=4)
