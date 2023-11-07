class cEnfermedad:
    # factor de riesgo
    ninguno = 0
    diabetes = 1
    obesidad = 2
    mayor_edad = 3
    enf_respiratoria = 4
    enf_cardiovascular = 5
    embarazo = 6
    def __init__(self, color: str, duracion: int, enfermedad: str, prioridad: int, tiempo_restante:int):
        self.color=color
        self.duracion=duracion
        self.enfermedad=enfermedad
        self.prioridad=prioridad
        self.tiempo_restante=tiempo_restante

    @staticmethod
    def convert_fr(factor_riesgo: str) -> int:
        valor: int = 0
        if factor_riesgo == "embarazo":
            valor = cEnfermedad.embarazo
        elif factor_riesgo == "enf_cardiovascular":
            valor = cEnfermedad.enf_cardiovascular
        elif factor_riesgo == "enf_respiratoria":
            valor = cEnfermedad.enf_respiratoria
        elif factor_riesgo == "mayor_edad":
            valor = cEnfermedad.mayor_edad
        elif factor_riesgo == "obesidad":
            valor = cEnfermedad.obesidad
        elif factor_riesgo == "diabetes":
            valor = cEnfermedad.diabetes
        elif factor_riesgo == "ninguno":
            valor = cEnfermedad.ninguno

        return valor
