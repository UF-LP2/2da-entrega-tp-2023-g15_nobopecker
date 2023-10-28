from enums import eEstado
from enums import eSintomas
from classEnfermedad import cEnfermedad
class cPaciente:

    def __init__(self, ID, sintomas:eSintomas, diagnostico:cEnfermedad, estado=eEstado.enfermo):
        self.ID=ID
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado


