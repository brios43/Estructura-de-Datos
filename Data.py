from Clases import *
import csv

class Dataset:
    def __init__(self):
        self.proyectos = listaenlazada()
        self.participantes = []
        self.disciplinas_proyectos = []
        self.tipos_proyecto = []
        self.monedas = []
        self.funciones = []
        self.estados_proyecto = []
        self.ref_disciplina = []

    def cargar_datos(self):
        proyectos = leer_archivo_csv('proyectos_2015.csv') + leer_archivo_csv('proyectos_2016.csv') + leer_archivo_csv('proyectos_2017.csv')+ leer_archivo_csv('proyectos_2018.csv') 
        participantes = leer_archivo_csv('proyecto_participante.csv')
        proyecto_disciplinas = leer_archivo_csv('proyecto_disciplina.csv')
        ref_tipos_proyecto = leer_archivo_csv('ref_tipo_proyecto.csv')
        ref_moneda = leer_archivo_csv('ref_moneda.csv')
        ref_funcion = leer_archivo_csv('ref_funcion.csv')
        ref_estado_proyecto = leer_archivo_csv('ref_estado_proyecto.csv')
        ref_disciplina = leer_archivo_csv('ref_disciplina.csv')

        for proyecto in proyectos:
            self.proyectos.add_to_end(Proyecto(*proyecto))
        for participante in participantes:
            self.participantes.append(Proyecto_Participante(*participante))
        for disciplina in proyecto_disciplinas:
            self.disciplinas_proyectos.append(Proyecto_disciplina(*disciplina))
        for tipo_proyecto in ref_tipos_proyecto:
            self.tipos_proyecto.append(Ref_tipo_proyecto(*tipo_proyecto))
        for moneda in ref_moneda:
            self.monedas.append(Ref_moneda(*moneda))
        for funcion in ref_funcion:
            self.funciones.append(Ref_funcion(*funcion))
        for estado_proyecto in ref_estado_proyecto:
            self.estados_proyecto.append(Ref_estadoProyecto(*estado_proyecto))
        for disciplina in ref_disciplina:
            self.ref_disciplina.append(Ref_disciplina(*disciplina))

    def distribucion_area(self):#1
        id_proyectos = []
        for proyecto in self.proyectos.iterate():
            id_proyectos.append(proyecto.proyecto_id) # Lista de id de proyectos para saber cuales tenemos
        disciplinas = {}
        for proyecto in self.disciplinas_proyectos:
            if proyecto.proyecto_id in id_proyectos:
                if proyecto.disciplina_id in disciplinas:
                    disciplinas[proyecto.disciplina_id] += 1
                else:
                    disciplinas[proyecto.disciplina_id] = 1
        areas = {}
        for ref_disciplina in self.ref_disciplina:
            if ref_disciplina.gran_area_descripcion not in areas:
                areas[ref_disciplina.gran_area_descripcion] = {ref_disciplina.area_descripcion:0}
            else:
                areas[ref_disciplina.gran_area_descripcion][ref_disciplina.area_descripcion] = 0
        for disciplina in disciplinas:
            for ref_disciplina in self.ref_disciplina:
                if disciplina == ref_disciplina.disciplina_id:
                    areas[ref_disciplina.gran_area_descripcion][ref_disciplina.area_descripcion] += disciplinas[disciplina]
        b,llaves=1,list(areas.keys())[1:]
        print("\nGran areas disponibles: ")
        for a in llaves:
                print(f"{b}. {a}")
                b+=1
        gran_area_elegida = input("ingrese gran area a mostrar: ")
        while gran_area_elegida not in ["1","2","3","4","5","6"]: #validacion
            gran_area_elegida = input("ingreso invalido, ingrese gran area a mostrar: ")
        gran_area_elegida = llaves[int(gran_area_elegida)-1]
        print(f"\nGran area: {gran_area_elegida}")
        for area in areas[gran_area_elegida]:
            print(f"Sub area: {area} - Cantidad de proyectos: {areas[gran_area_elegida][area]}")

    def cant_hombres_vs_cant_mujeres(self):#2
        hombres = 0
        mujeres = 0
        for proyecto in self.proyectos.iterate():
            #al ser string, hay que convertirlos a int, debemos corroborar de que no este vacio
            hombres += int(proyecto.cantidad_miembros_M) if proyecto.cantidad_miembros_M else 0
            mujeres += int(proyecto.cantidad_miembros_F) if proyecto.cantidad_miembros_F else 0
        if hombres+mujeres == 0:
            print('No hay datos de cantidad de hombres y mujeres')
        else:
            print(f'Porcentaje de mujeres: {round((mujeres/(hombres+mujeres))*100,2)}%')

    def promedio_tardanza_proyecto_por_area(self):#3
        areas = {}
        for disciplina in self.ref_disciplina:
            if disciplina.area_descripcion not in areas:
                areas[disciplina.area_descripcion] = [dt.timedelta(0),0]
        for proyecto in self.proyectos.iterate():
            for disciplina in self.disciplinas_proyectos:
                if proyecto.proyecto_id == disciplina.proyecto_id:
                    for ref_disciplina in self.ref_disciplina:
                        if disciplina.disciplina_id == ref_disciplina.disciplina_id:
                            if proyecto.fecha_finalizacion != "":
                                areas[ref_disciplina.area_descripcion][0] += dt.datetime.strptime(proyecto.fecha_finalizacion, '%Y/%m/%d %H:%M:%S.%f') - dt.datetime.strptime(proyecto.fecha_inicio, '%Y/%m/%d %H:%M:%S.%f')
                                areas[ref_disciplina.area_descripcion][1] += 1
        for area in areas:
            if areas[area][1] == 0:
                print(f'Area: {area} - Promedio: 0 dias')
            else:
                print(f'Area: {area} - Promedio: {((areas[area][0])/areas[area][1]).days} dias')
        
    def diferencia_montos(self):#5

        diferencia = 0
        for proyecto in self.proyectos.iterate():
            diferencia += int(float(proyecto.monto_total_solicitado)) - int(float(proyecto.monto_total_adjudicado))
        print(f'La diferencia entre el monto total solicitado y el monto total otorgado es: $ {diferencia}')

    def porcentaje_proyectos_innovacion(self):#6
        proyectos_innovacion = 0
        tipos_proyectos_innovadores = []
        for tipo_proyecto in self.tipos_proyecto:
            if tipo_proyecto.tipo_proyecto_cyt_desc == 'Tecnología e Innovación':
                tipos_proyectos_innovadores.append(tipo_proyecto.id)

        for proyecto in self.proyectos.iterate():
            if proyecto.tipo_proyecto_id in tipos_proyectos_innovadores:
                proyectos_innovacion += 1
        porcentaje = proyectos_innovacion/len(self.proyectos)*100
        print(f'El porcentaje de proyectos de innovacion es: {round(porcentaje,2)}%')

# FUNCIONES AUXILIARES
def leer_archivo_csv(nombre_archivo, encoding='utf-8'):
    datos = []
    try:
        with open(nombre_archivo, 'r', newline='', encoding=encoding) as archivo_csv:
            lector_csv = csv.reader(archivo_csv, delimiter=';')  # Especifica el delimitador como ;
            next(lector_csv)  # Omitir la primera fila (cabecera)
            for fila in lector_csv:
                datos.append(fila)
        return datos
    except FileNotFoundError:
        print(f'No se encontro el archivo o carpeta {nombre_archivo}')
        return None
