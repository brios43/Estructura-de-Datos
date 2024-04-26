from Data import Dataset
def main():
    #SE CREA UN OBJETO DATASET Y SE CARGAN LOS DATOS
    dataset = Dataset()
    dataset.cargar_datos()
    while True:
        print("\n1 - Distribucion proyectos por area")
        print("2 - Porcentaje de Mujeres")
        print("3 - Promedio de tardanza de proyecto por area")
        print("4 - Lista ordenada por fecha de inicio")
        print("5 - Diferencia de montos")
        print("6 - Porcentaje de proyectos de innovacion")
        print("7 - Salir")
        print("\n")
        opcion = input("Elige una opcion a ejecutar: ")
        print("\n")
        if opcion == "1":
            dataset.distribucion_area() 
        elif opcion == "2":  
            dataset.cant_hombres_vs_cant_mujeres()
        elif opcion == "3":
            dataset.promedio_tardanza_proyecto_por_area()
        elif opcion == "4":
            dataset.proyectos.lista_por_inicio()
        elif opcion == "5":
            dataset.diferencia_montos()
        elif opcion == "6":
            dataset.porcentaje_proyectos_innovacion()
        elif opcion == "7":
            print("\nPrograma cerrado con exito!")
            break
        else:
            print("\nOpcion inexistente, ingrese opción valida\n")


if __name__ == '__main__':
    main()