import json
import os
from datetime import datetime
from services.historia_clinica_service import load_data as load_historias
PACIENTES_FILE = "jsons/paciente.json"

"CARGA LOS DATOS DEL JSON"
def load_data():
    if not os.path.exists(PACIENTES_FILE):
        return []
    with open(PACIENTES_FILE, 'r', encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
            
"GUARDA LOS DATOS EN EL JSON"
def save_data(datos):
    with open(PACIENTES_FILE, 'w', encoding="utf-8") as file:
        return json.dump(datos,file,indent=4)    
   
"GUARDAR PACIENTE"
def save_paciente(dni, apellido, nombre, fecha_nac, nacionalidad):
    
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
    return print("Paciente guardado con éxito.")

"TRAER PACIENTES"
def get_pacientes():
    return print(load_data())

"TRAER PACIENTE POR ID"
def get_paciente_by_id(id_paciente):
    datos = load_data()
    for paciente in datos:
        if paciente.get('id_paciente') == id_paciente:
            return print(paciente)
    return print("Paciente no encontrado")

"EDITAR PACIENTE"
def edit_paciente(id_paciente, **kwargs):
    datos = load_data()
    for paciente in datos:
        if paciente.get('id_paciente') == id_paciente:
            for key, value in kwargs.items():
                if key in paciente:
                    paciente[key] = value
            save_data(datos)
            return print("Paciente editado con éxito")
    return print("Paciente no encontrado")


"ELIMINAR PACIENTE POR ID"
def delete_paciente_by_id(id_paciente):
    datos = load_data()
    for paciente in datos:
        if paciente.get('id_paciente') == id_paciente:
            datos.remove(paciente)
            save_data(datos)
            return print("Paciente eliminado con éxito")
    return print("Paciente no encontrado")

"BUSCAR POR NOMBRE"
def get_pacientes_by_name(nombre):

    datos = load_data()
    pacientes = []

    for paciente in datos:
        if nombre.lower() in paciente.get('nombre', '').lower():
            pacientes.append(paciente)

    return print(pacientes)

"BUSCAR POR APELLIDO"
def get_pacientes_by_lastname(apellido):
    datos = load_data()    
    pacientes = []

    for paciente in datos:
        if apellido.lower() in paciente.get('apellido', '').lower():
            pacientes.append(paciente)
    return pacientes

"BUSCAR POR RANGO DE FECHA"

def get_pacientes_atendidos_por_fecha(fecha_inicio, fecha_fin):
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()
    historias = load_historias()
    ids_pacientes = set()
    for historia in historias:
        fecha_historia = datetime.strptime(historia.get('fecha', ''), "%Y-%m-%d").date()
        if fecha_inicio <= fecha_historia <= fecha_fin:
            ids_pacientes.add(historia.get('id_paciente'))
    pacientes = load_data()
    pacientes_filtrados = []
    for paciente in pacientes:
        if paciente.get('id_paciente') in ids_pacientes:
            pacientes_filtrados.append(paciente)

    return print(pacientes_filtrados)

