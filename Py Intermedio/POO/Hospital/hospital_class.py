class Sala:
    def __init__(self, nombre, cant_camas, cant_pacientes):
        self.nombre = nombre
        self.cant_camas = cant_camas
        self.cant_pacientes = cant_pacientes

    def indicador_calidad(self):
        pass

class Terapia(Sala):
    def __init__(self, nombre, cant_camas, cant_pacientes, estado):
        super().__init__(nombre,cant_camas,cant_pacientes)
        self.estado = estado
    def indicador_calidad(self):
        if self.estado == 'bueno':
            return True
        else:
            return False
            

class General(Sala):
    def __init__(self,nombre,cant_camas, cant_pacientes, nombre_medico):
        super().__init__(nombre, cant_camas, cant_pacientes)
        self.nombre_medico = nombre_medico
    def indicador_calidad(self):
        if self.cant_camas >= self.cant_pacientes and self.nombre_medico != '':
            return True
        else:
            return False
        
class Controlador:
    lista_polimorfica = [] #almacena cualquier conjunto de datos independiente de la clase.

    def adicionar_sala(self,elemento):
        self.lista_polimorfica.append(elemento)
    
    def cantidad_IC(self):      #cantidad de salas que cumplen con el indicador de calidad.
        cantidad = 0
        for i in self.lista_polimorfica:
            if isinstance(i,General) and i.indicador_calidad()==True:       #'isinstance' permite reconocer instancia de clase específica.
                cantidad +=1
            elif isinstance(i,Terapia) and i.indicador_calidad() == True:
                cantidad+=1
        return cantidad
    
    def listar_mal_estado(self):
        lista_mal_estado = []
        for i in self.lista_polimorfica:
            if isinstance(i,Terapia) and i.estado == 'malo':
                lista_mal_estado.append(i)
        return lista_mal_estado
    
#instancia de clases
clase_a= Sala('Arcoiris', 6, 4)
print(clase_a.nombre)

clase_b = General('Gral',10,8,'Coria Ezequiel')
#print(clase_b.indicador_calidad())

clase_c = Terapia('Silence',15, 19, 'malo')
#print(clase_c.indicador_calidad())

clase_controladora = Controlador    ()
clase_controladora.adicionar_sala(clase_b)
clase_controladora.adicionar_sala(clase_c)
print(clase_controladora.lista_polimorfica)
print(clase_controladora.listar_mal_estado(), clase_controladora.cantidad_IC())