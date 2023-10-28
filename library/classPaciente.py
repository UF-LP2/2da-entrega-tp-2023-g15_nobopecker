from enums import eEstado
from library import enums
class cPaciente:

    def __init__(self, ID, sintomas, diagnostico, estado=eEstado.enfermo):
        self.ID=ID
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado


