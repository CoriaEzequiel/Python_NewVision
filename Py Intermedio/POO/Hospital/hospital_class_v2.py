class Sala:
    def __init__(self, nombre, cant_camas, cant_pacientes):
        self.nombre = nombre
        self.cant_camas = cant_camas
        self.cant_pacientes = cant_pacientes

    def indicador_calidad(self):
        pass

    def __str__(self):
        return f"Sala: {self.nombre}, Camas: {self.cant_camas}, Pacientes: {self.cant_pacientes}"


class Terapia(Sala):
    def __init__(self, nombre, cant_camas, cant_pacientes, estado):
        super().__init__(nombre, cant_camas, cant_pacientes)
        self.estado = estado

    def indicador_calidad(self):
        return self.estado == 'bueno'

    def __str__(self):
        return f"Terapia: {self.nombre}, Camas: {self.cant_camas}, Pacientes: {self.cant_pacientes}, Estado: {self.estado}"


class General(Sala):
    def __init__(self, nombre, cant_camas, cant_pacientes, nombre_medico):
        super().__init__(nombre, cant_camas, cant_pacientes)
        self.nombre_medico = nombre_medico

    def indicador_calidad(self):
        return self.cant_camas >= self.cant_pacientes and self.nombre_medico != ''

    def __str__(self):
        return f"General: {self.nombre}, Camas: {self.cant_camas}, Pacientes: {self.cant_pacientes}, Médico: {self.nombre_medico}"


class Controlador:
    lista_polimorfica = []  
    def adicionar_sala(self, elemento):
        self.lista_polimorfica.append(elemento)

    def cantidad_IC(self):
        cantidad = 0
        for i in self.lista_polimorfica:
            if isinstance(i, (General, Terapia)) and i.indicador_calidad():
                cantidad += 1
        return cantidad

    def listar_mal_estado(self):
        return [i for i in self.lista_polimorfica if isinstance(i, Terapia) and i.estado == 'malo']


# Instancias de prueba
clase_a = Sala('Arcoiris', 6, 4)
print(clase_a)

clase_b = General('Gral', 10, 8, 'Coria Ezequiel')
clase_c = Terapia('Silence', 15, 19, 'malo')

clase_controladora = Controlador()
clase_controladora.adicionar_sala(clase_b)
clase_controladora.adicionar_sala(clase_c)

# 15 instancias más (diversidad de situaciones)
nuevas_salas = [
    General("Gral Norte", 8, 8, "Dra. Laura"),
    General("Gral Sur", 10, 9, "Dr. Gómez"),
    General("Gral Oeste", 7, 8, ""),
    Terapia("Terapia 1", 5, 4, "bueno"),
    Terapia("Terapia 2", 5, 7, "malo"),
    Terapia("Terapia 3", 6, 5, "bueno"),
    Terapia("Terapia 4", 3, 3, "malo"),
    Terapia("Terapia 5", 10, 10, "bueno"),
    General("Gral Este", 5, 4, "Dr. Ramírez"),
    General("Gral Centro", 2, 1, "Dra. Paz"),
    Terapia("Terapia 6", 8, 9, "malo"),
    Terapia("Terapia 7", 8, 8, "bueno"),
    General("Gral X", 10, 15, "Dr. X"),
    Terapia("Terapia 8", 5, 3, "bueno"),
    General("Gral Y", 12, 11, "")
]

for sala in nuevas_salas:
    clase_controladora.adicionar_sala(sala)

print("\n--- Lista de todas las salas ---")
for sala in clase_controladora.lista_polimorfica:
    print(sala)

print("\n--- Salas de Terapia en mal estado ---")
for sala in clase_controladora.listar_mal_estado():
    print(sala)

print("\nCantidad de salas con indicador de calidad POSITIVO:", clase_controladora.cantidad_IC())