class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for row in data:
            values = row.split()
           
            if len(values) != len(self.FIELDS):
                continue
            record = dict(zip(self.FIELDS, values))
            self.lst_data.append(record)

    def select(self, a, b):
        
        if b >= len(self.lst_data):
            b = len(self.lst_data) - 1
        
        return self.lst_data[a:b+1]