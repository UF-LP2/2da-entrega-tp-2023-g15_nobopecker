from enums import eEstado
class cPaciente:

    def __init__(self, ID, sintomas, diagnostico, estado=eEstado.enfermo):
        self.ID=ID
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado


