from src.classEnfermedad import cEnfermedad
class cPaciente:

    def __init__(self, ID, nombre_apellido:str, diagnostico:cEnfermedad, factor_riesgo: str, sintomas:list[str], estado="enfermo"):
        self.ID=ID
        self.nombre_apellido=nombre_apellido
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado
        self.factor_riesgo=factor_riesgo


