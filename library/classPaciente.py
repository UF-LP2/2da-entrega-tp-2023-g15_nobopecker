from library.classEnfermedad import cEnfermedad
class cPaciente:

    def __init__(self, ID, nombre_apellido:str, diagnostico:cEnfermedad, factor_riesgo: str, sintomas:list[str], estado="enfermo"):
        self.ID=ID
        self.nombre_apellido=nombre_apellido
        self.sintomas=sintomas
        self.diagnostico=diagnostico
        self.estado=estado
        self.factor_riesgo=factor_riesgo

    def __lt__(self,other): #sobrecarga del < para poder comparar pacientes entre si segun su prioridad
        riesgo_propio=cEnfermedad.convert_fr(self.factor_riesgo)
        riesgo_otro=cEnfermedad.convert_fr(other.factor_riesgo)
        return True if (self.diagnostico.prioridad+riesgo_propio)<(other.diagnostico.prioridad +riesgo_otro) else False

