import heapq
from library.classPaciente import cPaciente
class PriorityQueuePaciente: #PriorityQueue que almacena pacientes
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, priority, item:cPaciente):
        heapq.heappush(self.elements, (-priority, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("La cola de prioridad está vacía")
        return heapq.heappop(self.elements)[1]
