from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message, owner_name):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass
