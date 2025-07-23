from services.paciente_service import *
from services.medico_service import save_medico, get_medicos
from services.historia_clinica_service import *

def menu():
    while True:
        print("----- Menú Principal -----")
        print("1. Listar pacientes")
        print("2. Buscar paciente por ID")
        print("3. Buscar pacientes por nombre")
        print("4. Buscar pacientes por apellido")
        print("5. Agregar paciente")
        print("6. Editar paciente")
        print("7. Eliminar paciente")
        print("8. Pacientes atendidos por rango de fecha")
        print("9. Listar médicos")
        print("10. Agregar médico")
        print("11. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("-----Listar pacientes-----")
            get_pacientes()
        elif opcion == "2":
            print("-----Buscar paciente por ID-----")
            id_paciente = int(input("Ingrese ID del paciente: "))
            get_paciente_by_id(id_paciente)
        elif opcion == "3":
            print("-----Buscar pacientes por nombre-----")
            nombre = input("Ingrese nombre: ")
            get_pacientes_by_name(nombre)
        elif opcion == "4":
            print("-----Buscar pacientes por apellido-----")
            apellido = input("Ingrese apellido: ")
            print(get_pacientes_by_lastname(apellido))
        elif opcion == "5":
            print("-----Agregar paciente-----")
            print("Ingrese los datos del paciente:")
            dni = input("DNI: ")
            apellido = input("Apellido: ")
            nombre = input("Nombre: ")
            fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
            nacionalidad = input("Nacionalidad: ")
            save_paciente(dni, apellido, nombre, fecha_nac, nacionalidad)
        elif opcion == "6":
            print("-----Editar paciente-----")
            id_paciente = int(input("ID del paciente a editar: "))
            campo = input("Campo a editar (dni, apellido, nombre, fecha_nac, nacionalidad): ")
            valor = input(f"Nuevo valor para {campo}: ")
            edit_paciente(id_paciente, **{campo: valor})
        elif opcion == "7":
            print("-----Eliminar paciente-----")
            id_paciente = int(input("ID del paciente a eliminar: "))
            delete_paciente_by_id(id_paciente)
        elif opcion == "8":
            print("-----Pacientes atendidos por rango de fecha-----")
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
            fecha_fin = input("Fecha fin (YYYY-MM-DD): ")
            get_pacientes_atendidos_por_fecha(fecha_inicio, fecha_fin)
        elif opcion == "9":
            print("-----Listar médicos-----")
            get_medicos()
        elif opcion == "10":
            print("-----Agregar médico-----")
            nombre = input("Nombre del médico: ")
            especialidad = input("Especialidad: ")
            save_medico(nombre, especialidad)
        elif opcion == "11":
            print("Saliendo del programa...")
            break
        else:
            print("Elija una opción válida.")

if __name__ == "__main__":
    menu()