class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for record in data:
            values = record.split()
            # Создаём словарь, сопоставляя поля и значения
            entry = dict(zip(self.FIELDS, values))
            self.lst_data.append(entry)

    def select(self, a, b):
        # Возвращаем копию среза, чтобы не изменять оригинал
        return self.lst_data[a:b+1] if b >= a else []