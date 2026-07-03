from abc import ABC, abstractmethod
from flowforge.context import Context


class Node(ABC):

    def __init__(self, node_id: str):
        self.node_id = node_id

    @abstractmethod
    def execute(self, context: Context) -> None:
        """
        Apenas side effects.
        Não retorna fluxo.
        """
        pass