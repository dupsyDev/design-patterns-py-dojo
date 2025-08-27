from abc import ABC, abstractmethod


class PC():
    def __init__(self):
        self._items = []

    def add_component(self, item):
        self._items.append(item)

    def show_specs(self):
        return ", ".join(self._items)

class PCBuilder(ABC):

    @abstractmethod
    def add_cpu(self):
        pass

    @abstractmethod
    def add_ram(self):
        pass

    @abstractmethod
    def add_gpu(self):
        pass

    @abstractmethod
    def add_disk(self):
        pass

    @abstractmethod
    def add_os(self):
        pass

    @abstractmethod
    def build_pc(self):
        pass

class GamingPCBuilder(PCBuilder):
    
    def __init__(self):
        self._pc = PC()

    def add_cpu(self):
        self._pc.add_component("High-end CPU")
        return self

    def add_ram(self):
        self._pc.add_component("High RAM")
        return self

    def add_gpu(self):
        self._pc.add_component("Dedicated GPU")
        return self

    def add_disk(self):
        self._pc.add_component("SSD storage")
        return self

    def add_os(self):
        self._pc.add_component("Windows OS")
        return self

    def build_pc(self):
        return self._pc
    

class OfficePCBuilder(PCBuilder):
    def __init__(self):
        self._pc = PC()

    def add_cpu(self):
        self._pc.add_component("Mid-range CPU")
        return self

    def add_ram(self):
        self._pc.add_component("Moderate RAM")
        return self

    def add_gpu(self):
        self._pc.add_component("No GPU")
        return self

    def add_disk(self):
        self._pc.add_component("HDD storage")
        return self

    def add_os(self):
        self._pc.add_component("Linux OS")
        return self

    def build_pc(self):
        return self._pc
    
class BuilderDirector():

    def __init__(self, builder: PCBuilder):
        self._builder = builder
    
    def construct_pc(self):
        return self._builder.add_cpu().add_ram().add_gpu().add_disk().add_os().build_pc()


if __name__ == "__main__":
    office_pc_builder = OfficePCBuilder()
    gaming_pc_builder = GamingPCBuilder()

    office_pc_director = BuilderDirector(office_pc_builder)
    gaming_pc_director = BuilderDirector(gaming_pc_builder)

    office_pc = office_pc_director.construct_pc()
    gaming_pc = gaming_pc_director.construct_pc()

    print(f"Office PC specs: {office_pc.show_specs()}")
    print(f"Gaming PC specs: {gaming_pc.show_specs()}")