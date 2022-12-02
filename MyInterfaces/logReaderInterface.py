from abc import ABC, abstractmethod


class logReader(ABC):
    @abstractmethod
    def readline():
        return str | None

    @abstractmethod
    def close():
        pass
