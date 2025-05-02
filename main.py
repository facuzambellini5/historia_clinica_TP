import json
import os

PACIENTES_FILE = "pacientes.json"

def load_data():

    if not os.path.exists(PACIENTES_FILE):
        return []
    with open(PACIENTES_FILE, 'r', encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
            

def save_data(datos):
    with open(PACIENTES_FILE, 'w', encoding="utf-8") as file:
        return json.dump(datos,file,indent=4)    
   
"CREAR PACIENTE"
def crearPaciente(dni, apellido, nombre, fecha_nac, nacionalidad):
    
    datos = load_data()
    paciente = {
        "id_paciente": len(datos) + 1,
        "dni": dni,
        "apellido": apellido,
        "nombre": nombre,
        "fecha_nac": fecha_nac,
        "nacionalidad": nacionalidad
    }
    
    datos.append(paciente)
    save_data(datos)
    return paciente

"TRAER PACIENTES"
def getPacientes():
    return load_data()


def get_paciente_by_id(id_paciente):
    datos = load_data()
    for paciente in datos:
        if paciente.get('id_paciente') == id_paciente:
            return paciente
    return "Paciente no encontrado"

def edit_paciente(id_paciente, **kwargs):
    datos = load_data()
    for paciente in datos:
        if paciente.get('id_paciente') == id_paciente:
            for key, value in kwargs.items():
                if key in paciente:
                    paciente[key] = value
            save_data(datos)
            return "Paciente editado con éxito"
    return "Paciente no encontrado"


"ELIMINAR PACIENTE"
def delete_by_id(id_paciente):
    datos = load_data()
    for paciente in datos:
        if paciente.get('id_paciente') == id_paciente:
            datos.remove(paciente)
            save_data(datos)
            return "Paciente eliminado con éxito"
    return "Paciente no encontrado"

    
"BUSCAR POR NOMBRE"
def get_pacientes_by_name(nombre):

    datos = load_data()
    pacientes = []

    for paciente in datos:
        if nombre.lower() in paciente.get('nombre', '').lower():
            pacientes.append(paciente)

    return pacientes

"BUSCAR POR APELLIDO"
def get_pacientes_by_lastname(apellido):
    datos = load_data()
    pacientes = []

    for paciente in datos:
        if apellido.lower() in paciente.get('apellido', '').lower():
            pacientes.append(paciente)
    return pacientes
        
"CREAR, TRAER, EDITAR, ELIMINAR"

print(delete_by_id(8))
"""print(getPacientes())"""
