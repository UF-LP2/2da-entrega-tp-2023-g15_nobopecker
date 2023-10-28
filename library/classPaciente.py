from enums import eEstado
from enums import eColor
from enums import eSintomas_Enfermedades
class cPaciente:

    def __init__(self, ID, sintomas:eSintomas_Enfermedades, diagnostico:eSintomas_Enfermedades, estado=eEstado.enfermo):
        self.ID=ID
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado


