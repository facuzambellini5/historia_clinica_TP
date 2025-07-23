import json
import os

MEDICOS_FILE = "jsons/medico.json"

"CARGA LOS DATOS DEL JSON"
def load_data():
    if not os.path.exists(MEDICOS_FILE):
        return []
    with open(MEDICOS_FILE, 'r', encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
            
"GUARDA LOS DATOS EN EL JSON"
def save_data(datos):
    with open(MEDICOS_FILE, 'w', encoding="utf-8") as file:
        return json.dump(datos,file,indent=4)

"GUARDAR MEDICO"
def save_medico(apellido, nombre, especialidad):

    datos = load_data()
    medico = {
        "id_medico": len(datos) + 1,
        "apellido": apellido,
        "nombre": nombre,
        "especialidad": especialidad
    }

    datos.append(medico)
    save_data(datos)
    return print("Medico guardado con éxito.")

"TRAER MEDICOS"
def get_medicos():
    return print(load_data())

"TRAER MEDICO POR ID"
def get_medico_by_id(id_medico):
    datos = load_data()
    for medico in datos:
        if medico.get('id_medico') == id_medico:
            return print(medico)
    return print("Medico no encontrado")

"EDITAR MEDICO"
def edit_medico(id_medico, **kwargs):
    datos = load_data()
    for medico in datos:
        if medico.get('id_medico') == id_medico:
            for key, value in kwargs.items():
                if key in medico:
                    medico[key] = value
            save_data(datos)
            return print("Medico editado con éxito")
    return print("Medico no encontrado")


"ELIMINAR MEDICO POR ID"
def delete_medico_by_id(id_medico):
    datos = load_data()
    for medico in datos:
        if medico.get('id_medico') == id_medico:
            datos.remove(medico)
            save_data(datos)
            return print("Medico eliminado con éxito")
    return print("Medico no encontrado")

"BUSCAR POR NOMBRE"
def get_medicos_by_name(nombre):

    datos = load_data()
    medicos = []

    for medico in datos:
        if nombre.lower() in medico.get('nombre', '').lower():
            medicos.append(medico)

    return print(medicos)

"BUSCAR POR APELLIDO"
def get_medicos_by_lastname(apellido):
    datos = load_data()    
    medicos = []

    for medico in datos:
        if apellido.lower() in medicos.get('apellido', '').lower():
            medicos.append(medico)
    return print(medicos)