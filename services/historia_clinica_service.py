import json
import os


HISTORIA_CLINICA = "historia_clinica.json"
PACIENTES_FILE = "pacientes.json"
MEDICOS_FILE = "medicos.json"


"CARGA LOS DATOS DEL JSON"
def load_data():
    if not os.path.exists(HISTORIA_CLINICA):
        return []
    with open(HISTORIA_CLINICA, 'r', encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
            
"GUARDA LOS DATOS EN EL JSON"
def save_data(datos):
    with open(HISTORIA_CLINICA, 'w', encoding="utf-8") as file:
        return json.dump(datos,file,indent=4) 
    
"GUARDAR HISTORIA_CLINICA"
def save_historia_clinica(fecha, enfermedad, id_medico, id_paciente, observaciones):
    
    datos = load_data()
    historia_clinica = {
        "id_historia": len(datos) + 1,
        "fecha": fecha,
        "enfermedad": enfermedad,
        "id_medico": id_medico,
        "id_paciente": id_paciente,
        "observaciones": observaciones
    }

    # Validar que el paciente y el médico existan
    with open(PACIENTES_FILE, 'r', encoding="utf-8") as file:
        pacientes = json.load(file)

    with open(MEDICOS_FILE, 'r', encoding="utf-8") as file:
        medicos = json.load(file)

    for paciente in pacientes:
        if paciente.get("id_paciente") != id_paciente:
            return "Paciente no encontrado."

    for medico in medicos:
        if medico.get("id_medico") != id_medico:
            return "Médico no encontrado."
        

    datos.append(historia_clinica)
    save_data(datos)
    return "Historia clínica guardada con éxito."

"TRAER HISTORIA_CLINICA"
def get_historia_clinica():
    return load_data()

"TRAER HISTORIA_CLINICA POR ID"
def get_historia_clinica_by_id(id_historia):
    datos = load_data()
    for historia in datos:
        if historia.get("id_historia") == id_historia:
            return historia
    else:
        return "Historia clínica no encontrada"

"EDITAR HISTORIA_CLINICA"
def edit_historia_clinica(id_historia, **kwargs):
    datos = load_data()
    for historia in datos:
        if historia.get('id_historia') == id_historia:
            for key, value in kwargs.items():
                if key in historia:
                    historia[key] = value
            save_data(datos)
            return "Historia clínica editada con éxito"
        else:  
            return "Historia clínica no encontrada"

"ELIMINAR HISTORIA_CLINICA"

def delete_historia_clinica(id_historia):
    datos = load_data()
    for historia in datos:
        if historia.get('id_historia') == id_historia:
            datos.remove(historia)
            save_data(datos)
            return "Historia clínica eliminada con éxito"
        else:
            return "Historia clínica no encontrada"