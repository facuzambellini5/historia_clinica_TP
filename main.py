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
    
crearPaciente(998,"Ravioli","Peperoni","10-03","Italiano")
print(getPacientes())