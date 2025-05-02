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
   

def crearPaciente(dni, apellido, nombre, fecha_nac, nacionalidad):
    
    datos = load_data()
    paciente = {
        "dni": dni,
        "apellido": apellido,
        "nombre": nombre,
        "fecha_nac": fecha_nac,
        "nacionalidad": nacionalidad
    }
    
    datos.append(paciente)
    save_data(datos)
    return paciente


def getPacientes():
    return load_data()
    

def get_pacientes_by_name(nombre):

    datos = load_data()
    pacientes = []

    for paciente in datos:
        if nombre.lower() in paciente.get('nombre', '').lower():
            pacientes.append(paciente)

    return pacientes


def get_pacientes_by_lastname(apellido):
    datos = load_data()
    pacientes = []

    for paciente in datos:
        if apellido.lower() in paciente.get('apellido', '').lower():
            pacientes.append(paciente)
    
    return pacientes
        





"""print(getPacientes())"""
print(get_pacientes_by_name('mile'))
print(get_pacientes_by_lastname('pepe'))