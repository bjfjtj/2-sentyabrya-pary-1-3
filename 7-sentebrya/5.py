class Dictionary:
    rus = "Питон"
    eng = "Python"
value = getattr(Dictionary, "rus_word", False)
print(value)