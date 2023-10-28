from enums import eEstado
from enums import eSintomas_Enfermedades
class cPaciente:

    def __init__(self, ID, sintomas, diagnostico:eSintomas_Enfermedades, estado=eEstado.enfermo):
        self.ID=ID
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado


