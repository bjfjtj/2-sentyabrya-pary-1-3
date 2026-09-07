class Graph:
    def __init__(self, data):
        self.data = data[:]
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def set_show(self, fl_show):
        self.is_show = fl_show

    def _format_data(self):
        return ' '.join(map(str, self.data))

    def show_table(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print(self._format_data())

    def show_graph(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print(f"Графическое отображение данных: {self._format_data()}")

    def show_bar(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print(f"Столбчатая диаграмма: {self._format_data()}")


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()