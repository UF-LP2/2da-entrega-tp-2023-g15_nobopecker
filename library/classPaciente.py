from classEnfermedad import cEnfermedad
class cPaciente:

    def __init__(self, ID, diagnostico:cEnfermedad, factor_riesgo: str, sintomas:list[str], estado="enfermo"):
        self.ID=ID
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado
        self.factor_riesgo=factor_riesgo


