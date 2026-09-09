class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, mem_slots):
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots[:4]  # обрезаем до 4, если больше

    def get_config(self):
        config = []
        config.append(f"Материнская плата: {self.name}")
        config.append(f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}")
        config.append(f"Слотов памяти: {len(self.mem_slots)}")
        memory_info = []
        for mem in self.mem_slots:
            memory_info.append(f"{mem.name} - {mem.volume}")
        config.append("Память: " + "; ".join(memory_info) if memory_info else "Память: отсутствует")
        return config