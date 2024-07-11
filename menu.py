from funciones import *

def menu():
    global proyectos

    while True:
        print("\nMenú:")
        print("1. Ingresar proyecto")
        print("2. Modificar proyecto")
        print("3. Cancelar proyecto")
        print("4. Comprobar proyectos")
        print("5. Mostrar todos")
        print("6. Calcular presupuesto promedio")
        print("7. Buscar proyecto por nombre")
        print("8. Ordenar proyectos")
        print("9. Retomar proyecto")
        print("10. Generar Reporte por Presupuesto")
        print("11. Generar Reporte por Nombre de Proyecto")
        print("12. Mostrar proyectos que hayan durado mas de dos años")
        print("13. Mostrar proyectos que hayan durado menos de tres años")
        print("0. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agregar_proyecto()
        elif opcion == 2:
            modificar_proyecto()
        elif opcion == 3:
            cancelar_proyecto()
        elif opcion == 4:
            comprobar_proyectos()
        elif opcion == 5:
            mostrar_todos()
        elif opcion == 6:
            calcular_presupuesto_promedio()
        elif opcion == 7:
            buscar_proyecto_por_nombre()
        elif opcion == 8:
            ordenar_proyectos()
        elif opcion == 9:
            retomar_proyecto()
        elif opcion == 10:
            generar_reporte_por_presupuesto() 
        elif opcion == 11:
            generar_reporte_por_nombre()   
        elif opcion == 12:
            mostrar_proyectos_finalizados_dos_anios()
        elif opcion == 13:
            mostrar_proyectos_finalizados_menos_tres_anios()        
        elif opcion == 0:
            guardar_proyectos_csv(proyectos, 'Proyectos.csv')
            guardar_proyectos_finalizados_json(proyectos)
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
