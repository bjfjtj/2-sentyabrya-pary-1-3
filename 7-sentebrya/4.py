class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

author_value = getattr(Notes, "author")
print(author_value)