class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng):
        if eng in self.tr:
            return self.tr[eng]
        else:
            return False
tr = Translator()
pairs = [
    ('tree', 'дерево'),
    ('car', 'машина'),
    ('car', 'автомобиль'),
    ('leaf', 'лист'),
    ('river', 'река'),
    ('go', 'идти'),
    ('go', 'ехать'),
    ('go', 'ходить'),
    ('milk', 'молоко')
]

for eng, rus in pairs:
    tr.add(eng, rus)
tr.remove('car')
result = tr.translate('go')
if isinstance(result, list):
    print(' '.join(result))
else:
    print(result)