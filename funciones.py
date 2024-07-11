import csv
import json
import os
from datetime import datetime

# Lee archivo csv
def cargar_proyectos_desde_csv(ruta_csv):
    proyectos = []
    if os.path.exists(ruta_csv):
        with open(ruta_csv,"r", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                proyectos.append(row)  

    return proyectos

# Validaciones
def validar_nombre_proyecto(nombre: str):
    if len(nombre) > 30:
        print("Error, el nombre de su proyecto no puede superar los 30 caracteres")
        return False
    for caracter in nombre:
        if not caracter.isalpha():
            print("Error, el nombre de su proyecto debe tener solo caracteres alfabeticos")
            return False
    return True

def validar_descripcion_proyecto(descripcion: str):
    if len(descripcion) > 200:
        print("Error, la descripcion de su proyecto no puede superar los 200 caracteres")
        return False
    for caracter in descripcion:
        if not caracter.isalnum() and not caracter.isspace():
            print("Error, la descripcion de su proyecto debe ser alfanumerica")
            return False
    return True

def validar_presupuesto_proyecto(presupuesto: str):
    if presupuesto.isdigit():
        presupuesto_entero = int(presupuesto)
        if presupuesto_entero >= 500000:
            return True 
        else:
            print("Error, ingrese un presupuesto mayor o igual a 500000")
    else:
        print("Error, el valor del presupuesto debe ser entero")
    return False

def validar_formato_fechas(fecha: str):
    partes = fecha.split("-")
    if len(partes) != 3:
        return False

    dia, mes, anio = partes
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False

    dia, mes, anio = int(dia), int(mes), int(anio)

    if anio < 1 or anio > 9999:
        print("Error, ingrese el año entre 1 y 9999")
        return False

    if mes < 1 or mes > 12:
        print("Error, ingrese un mes del 1 y 12")
        return False
    
    if dia < 1 or dia > 31:
        print("Error, ingrese un dia del 1 al 31")
        return False

    return True

def comparar_fechas_inicio_fin(fecha_inicio: str, fecha_fin: str):
    if not (validar_formato_fechas(fecha_inicio) and validar_formato_fechas(fecha_fin)):
        print("Error, formato de fechas inválido")
        return False

    dia_inicio, mes_inicio, anio_inicio = map(int, fecha_inicio.split("-"))
    dia_fin, mes_fin, anio_fin = map(int, fecha_fin.split("-"))

    fecha_inicio_obj = datetime(anio_inicio, mes_inicio, dia_inicio)
    fecha_fin_obj = datetime(anio_fin, mes_fin, dia_fin)

    if fecha_fin_obj < fecha_inicio_obj:
        print("Error, la fecha de fin no puede ser anterior a la fecha de inicio.")
        return False

    return True   

def validar_estado(estado: str):
    estados_permitidos = ['Activo', 'Cancelado', 'Finalizado']
    if estado in estados_permitidos:
        return True
    else:
        print("Error, ingrese el estado nuevamente")
        return False 

def agregar_proyecto():
    if len(proyectos) >= 50:
        print("No se pueden agregar más proyectos. Límite alcanzado.")
        return

    nombre = input("Nombre del Proyecto: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha de Inicio (DD-MM-AAAA): ")
    fecha_fin = input("Fecha de Fin (DD-MM-AAAA): ")
    presupuesto = input("Presupuesto: ")
    estado = input("Estado: ")

    if not validar_nombre_proyecto(nombre):
        return
    if not validar_descripcion_proyecto(descripcion):
        return
    if not validar_presupuesto_proyecto(presupuesto):
        return
    if not comparar_fechas_inicio_fin(fecha_inicio, fecha_fin):
        return
    if not validar_estado(estado):
        return

    # ID autoincremental
    id_proyecto = len(proyectos) + 1
    proyecto = {
        "id": id_proyecto,
        "Nombre del Proyecto": nombre,
        "Descripción": descripcion,
        "Fecha de inicio": fecha_inicio,
        "Fecha de Fin": fecha_fin,
        "Presupuesto": presupuesto,
        "Estado": estado
    }
    proyectos.append(proyecto)
    print("Proyecto agregado exitosamente.")

def modificar_proyecto():
    id_proyecto = int(input("Ingrese el ID del proyecto a modificar: "))
    proyecto = None
    for p in proyectos:
        if p['id'] == str(id_proyecto):
            proyecto = p
            break
    if not proyecto:
        print("Proyecto no encontrado.")
        return

    print("Seleccione el dato a modificar:")
    print("1. Nombre del Proyecto")
    print("2. Descripción")
    print("3. Fecha de Inicio")
    print("4. Fecha de Fin")
    print("5. Presupuesto")
    print("6. Estado")
    opcion = int(input("Opción: "))

    if opcion == 1:
        nombre = input("Nuevo Nombre del Proyecto: ")
        if not nombre.isalpha() or len(nombre) > 30:
            print("Nombre del proyecto no válido.")
            return
        proyecto["Nombre del Proyecto"] = nombre
    elif opcion == 2:
        descripcion = input("Nueva Descripción: ")
        if len(descripcion) > 200:
            print("Descripción no válida.")
            return
        proyecto["Descripción"] = descripcion
    elif opcion == 3:
        fecha_inicio = input("Nueva Fecha de Inicio (DD/MM/AAAA): ")
        try:
            fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        except ValueError:
            print("Formato de fecha no válido.")
            return
        proyecto["Fecha de Inicio"] = fecha_inicio.strftime("%d/%m/%Y")
    elif opcion == 4:
        fecha_fin = input("Nueva Fecha de Fin (DD/MM/AAAA): ")
        try:
            fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        except ValueError:
            print("Formato de fecha no válido.")
            return
        proyecto["Fecha de Fin"] = fecha_fin.strftime("%d/%m/%Y")
    elif opcion == 5:
        presupuesto = int(input("Nuevo Presupuesto: "))
        if presupuesto < 500000:
            print("Presupuesto no válido.")
            return
        proyecto["Presupuesto"] = presupuesto
    elif opcion == 6:
        estado = input("Nuevo Estado (Activo/Cancelado/Finalizado): ")
        if estado not in ['Activo', 'Cancelado', 'Finalizado']:
            print("Estado no válido.")
            return
        proyecto["Estado"] = estado
    else:
        print("Opción no válida.")
        return

    print("Proyecto modificado exitosamente.")

def cancelar_proyecto():
    id_proyecto = int(input("Ingrese el ID del proyecto a cancelar: "))
    proyecto = None
    for p in proyectos:
        if p['id'] == str(id_proyecto):
            proyecto = p
            break
    if not proyecto:
        print("Proyecto no encontrado.")
        return

    proyecto["Estado"] = 'Cancelado'
    print("Proyecto cancelado exitosamente.")

def comprobar_proyectos():
    fecha_actual = datetime.now()
    for proyecto in proyectos:
        fecha_fin = datetime.strptime(proyecto['Fecha de Fin'], "%d-%m-%Y")
        if fecha_fin < fecha_actual:
            proyecto["Estado"] = 'Finalizado'
    print("Proyectos comprobados exitosamente.")

def mostrar_todos():
    if not proyectos:
        print("No hay proyectos registrados.")
        return

    print(f"| {'id'} | {'Nombre del Proyecto'} | {'Descripción'} | {'Fecha de inicio'} | {'Fecha de Fin'} | {'Presupuesto'} | {'Estado'} |")
    for proyecto in proyectos:
        print(f"| {proyecto['id']} | {proyecto['Nombre del Proyecto']} | {proyecto['Descripción']} | {proyecto['Fecha de inicio']} | {proyecto['Fecha de Fin']} |{proyecto['Presupuesto']} | {proyecto['Estado']} |")

def calcular_presupuesto_promedio():
    if not proyectos:
        print("No hay proyectos registrados.")
        return

    presupuesto_total = 0
    for proyecto in proyectos:
        presupuesto_total += int(proyecto['Presupuesto'])
    presupuesto_promedio = presupuesto_total / len(proyectos)
    print(f"Presupuesto promedio: ${presupuesto_promedio}")

def buscar_proyecto_por_nombre():
    nombre = input("Ingrese el nombre del proyecto a buscar: ")
    proyecto = None
    for p in proyectos:
        if p['Nombre del Proyecto'] == nombre:
            proyecto = p
            break
    if not proyecto:
        print("Proyecto no encontrado.")
        return

    print(f"ID: {proyecto['id']}")
    print(f"Nombre del Proyecto: {proyecto['Nombre del Proyecto']}")
    print(f"Descripción: {proyecto['Descripción']}")
    print(f"Fecha de Inicio: {proyecto['Fecha de inicio']}")
    print(f"Fecha de Fin: {proyecto['Fecha de Fin']}")
    print(f"Presupuesto: {proyecto['Presupuesto']}")
    print(f"Estado: {proyecto['Estado']}")

# Funciones para ordenar proyectos
def ordenar_por_nombre(proyecto):
    return proyecto['Nombre del Proyecto']

def ordenar_por_presupuesto(proyecto):
    return int(proyecto['Presupuesto'])

def ordenar_por_fecha_inicio(proyecto):
    return datetime.strptime(proyecto['Fecha de inicio'], "%d-%m-%Y")

def ordenar_proyectos():
    print("Seleccione el criterio de ordenación:")
    print("1. Nombre del Proyecto")
    print("2. Presupuesto")
    print("3. Fecha de Inicio")
    opcion = int(input("Opción: "))

    if opcion == 1:
        proyectos.sort(key=ordenar_por_nombre)
    elif opcion == 2:
        proyectos.sort(key=ordenar_por_presupuesto)
    elif opcion == 3:
        proyectos.sort(key=ordenar_por_fecha_inicio)
    else:
        print("Opción no válida.")
        return

    mostrar_todos()

def retomar_proyecto():
    id_proyecto = int(input("Ingrese el ID del proyecto a retomar: "))
    proyecto = None
    for p in proyectos:
        if p['id'] == str(id_proyecto) and p['Estado'] == 'Cancelado':
            proyecto = p
            break
    if not proyecto:
        print("Proyecto no encontrado o no está cancelado.")
        return
    
    estado = input("Ingrese el nuevo estado del proyecto (Activo/Finalizado): ")
    if estado not in ['Activo', 'Finalizado']:
        print("Estado no válido.")
        return

    proyecto["Estado"] = estado
    print("Proyecto retomado exitosamente.") 

def guardar_proyectos_csv(proyectos, ruta_csv):
    with open(ruta_csv, mode='w', newline='') as file:
        datos = ["id", "Nombre del Proyecto", "Descripción", "Fecha de Inicio", "Fecha de Fin", "Presupuesto", "Estado"]
        writer = csv.DictWriter(file, fieldnames=datos)
        writer.writeheader()
        for proyecto in proyectos:
            proyecto_lower = {
                "id": proyecto["id"],
                "Nombre del Proyecto": proyecto["Nombre del Proyecto"],
                "Descripción": proyecto["Descripción"],
                "Fecha de Inicio": proyecto["Fecha de inicio"],
                "Fecha de Fin": proyecto["Fecha de Fin"],
                "Presupuesto": proyecto["Presupuesto"],
                "Estado": proyecto["Estado"]
            }
        writer.writerow(proyecto_lower)

def guardar_proyectos_finalizados_json(proyectos):
    proyectos_finalizados = [proyecto for proyecto in proyectos if proyecto['Estado'] == 'Finalizado']
    with open('ProyectosFinalizados.json', 'w') as file:
        json.dump(proyectos_finalizados, file, indent=4)

def mostrar_proyectos_finalizados_dos_anios():
    proyectos_finalizados_dos_anios = []
    for proyecto in proyectos:
        if proyecto['Estado'] == 'Finalizado':
            fecha_inicio = datetime.strptime(proyecto['Fecha de inicio'], "%d-%m-%Y")
            fecha_fin = datetime.strptime(proyecto['Fecha de Fin'], "%d-%m-%Y")
            duracion = (fecha_fin - fecha_inicio).days / 365.25  # Convertir días a años
            if duracion > 2:
                proyectos_finalizados_dos_anios.append(proyecto)
    
    if not proyectos_finalizados_dos_anios:
        print("No hay proyectos finalizados que hayan durado más de 2 años.")
        return
    
    print(f"| {'id':<2} | {'Nombre del Proyecto':<30} | {'Descripción':<50} | {'Fecha de inicio':<12} | {'Fecha de Fin':<12} | {'Presupuesto':<10} | {'Estado':<10} |")
    for proyecto in proyectos_finalizados_dos_anios:
        print(f"| {proyecto['id']:<2} | {proyecto['Nombre del Proyecto']:<30} | {proyecto['Descripción']:<50} | {proyecto['Fecha de inicio']:<12} | {proyecto['Fecha de Fin']:<12} |{proyecto['Presupuesto']:<10} | {proyecto['Estado']:<10} |")

def mostrar_proyectos_finalizados_menos_tres_anios():
    proyectos_finalizados_menos_tres_anios = []
    for proyecto in proyectos:
        if proyecto['Estado'] == 'Finalizado':
            fecha_inicio = datetime.strptime(proyecto['Fecha de inicio'], "%d-%m-%Y")
            fecha_fin = datetime.strptime(proyecto['Fecha de Fin'], "%d-%m-%Y")
            duracion = (fecha_fin - fecha_inicio).days / 365.25  # Convertir días a años
            if duracion < 3:
                proyectos_finalizados_menos_tres_anios.append(proyecto)
    
    if not proyectos_finalizados_menos_tres_anios:
        print("No hay proyectos finalizados que hayan durado menos de 3 años.")
        return
    
    print(f"| {'id':<2} | {'Nombre del Proyecto':<30} | {'Descripción':<50} | {'Fecha de inicio':<12} | {'Fecha de Fin':<12} | {'Presupuesto':<10} | {'Estado':<10} |")
    for proyecto in proyectos_finalizados_menos_tres_anios:
        print(f"| {proyecto['id']:<2} | {proyecto['Nombre del Proyecto']:<30} | {proyecto['Descripción']:<50} | {proyecto['Fecha de inicio']:<12} | {proyecto['Fecha de Fin']:<12} |{proyecto['Presupuesto']:<10} | {proyecto['Estado']:<10} |")

numero_reporte = 1

def generar_reporte_por_presupuesto():
    global numero_reporte
    presupuesto = int(input("Ingrese el presupuesto a comparar: "))
    proyectos_superan_presupuesto = [p for p in proyectos if int(p['Presupuesto']) > presupuesto]

    if not proyectos_superan_presupuesto:
        print("No hay proyectos que superen ese presupuesto.")
        return

    fecha_solicitud = datetime.now().strftime("%d-%m-%Y")
    cantidad_proyectos = len(proyectos_superan_presupuesto)
    reporte = f"Reporte Número: {numero_reporte}\nFecha de Solicitud: {fecha_solicitud}\nCantidad de Proyectos: {cantidad_proyectos}\n\nListado de Proyectos:\n"
    reporte += f"| {'id'} | {'Nombre del Proyecto'} | {'Descripción'} | {'Fecha de inicio'} | {'Fecha de Fin'} | {'Presupuesto'} | {'Estado'} |\n"
    
    for proyecto in proyectos_superan_presupuesto:
        reporte += f"| {proyecto['id']} | {proyecto['Nombre del Proyecto']} | {proyecto['Descripción']} | {proyecto['Fecha de inicio']} | {proyecto['Fecha de Fin']} | {proyecto['Presupuesto']} | {proyecto['Estado']} |\n"

    with open(f"reporte_{numero_reporte}.txt", "w", encoding='utf-8') as file:
        file.write(reporte)

    numero_reporte += 1
    print(f"Reporte generado exitosamente como 'reporte_{numero_reporte - 1}.txt'.")

def generar_reporte_por_nombre():
    global numero_reporte
    nombre = input("Ingrese el nombre del proyecto a buscar: ")
    proyectos_con_nombre = []
    for p in proyectos:
        if p['Nombre del Proyecto'] == nombre:
            proyectos_con_nombre.append(p)

    if not proyectos_con_nombre:
        print("No hay proyectos con ese nombre.")
        return

    fecha_solicitud = datetime.now().strftime("%d-%m-%Y")
    cantidad_proyectos = len(proyectos_con_nombre)
    reporte = f"Reporte Número: {numero_reporte}\nFecha de Solicitud: {fecha_solicitud}\nCantidad de Proyectos: {cantidad_proyectos}\n\nListado de Proyectos:\n"
    reporte += f"| {'id'} | {'Nombre del Proyecto'} | {'Descripción'} | {'Fecha de inicio'} | {'Fecha de Fin'} | {'Presupuesto'} | {'Estado'} |\n"
    
    for proyecto in proyectos_con_nombre:
        reporte += f"| {proyecto['id']} | {proyecto['Nombre del Proyecto']} | {proyecto['Descripción']} | {proyecto['Fecha de inicio']} | {proyecto['Fecha de Fin']} | {proyecto['Presupuesto']} | {proyecto['Estado']} |\n"

    with open(f"reporte_nombre_{numero_reporte}.txt", "w", encoding='utf-8') as file:
        file.write(reporte)

    numero_reporte += 1
    print(f"Reporte generado exitosamente como 'reporte_nombre_{numero_reporte - 1}.txt'.")



proyectos = cargar_proyectos_desde_csv('proyecto_1/Proyectos.csv')    