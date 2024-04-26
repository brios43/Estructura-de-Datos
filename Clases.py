import datetime as dt
class Proyecto:
    def __init__(self, proyecto_id, proyecto_fuente, titulo, fecha_inicio, fecha_finalizacion, resumen, moneda_id, monto_total_solicitado, monto_total_adjudicado, monto_financiado_solicitado, monto_financiado_adjudicado, tipo_proyecto_id, codigo_identificacion, palabras_clave, estado_id, fondo_anpcyt, cantidad_miembros_F, cantidad_miembros_M, sexo_director):
        self.proyecto_id = proyecto_id
        self.proyecto_fuente = proyecto_fuente
        self.titulo = titulo
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.resumen = resumen
        self.moneda_id = moneda_id
        self.monto_total_solicitado = monto_total_solicitado
        self.monto_total_adjudicado = monto_total_adjudicado
        self.monto_financiado_solicitado = monto_financiado_solicitado
        self.monto_financiado_adjudicado = monto_financiado_adjudicado
        self.tipo_proyecto_id = tipo_proyecto_id
        self.codigo_identificacion = codigo_identificacion
        self.palabras_clave = palabras_clave
        self.estado_id = estado_id
        self.fondo_anpcyt = fondo_anpcyt
        self.cantidad_miembros_F = cantidad_miembros_F
        self.cantidad_miembros_M = cantidad_miembros_M
        self.sexo_director = sexo_director

class Proyecto_Participante:
    def __init__(self, proyecto_id,persona_id,funcion_id,fecha_inicio,fecha_fin):
        self.proyecto_id = proyecto_id
        self.persona_id = persona_id
        self.funcion_id = funcion_id
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

class Proyecto_disciplina:
    def __init__(self, proyecto_id,disciplina_id):
        self.proyecto_id = proyecto_id
        self.disciplina_id = disciplina_id

class Ref_tipo_proyecto:
    def __init__(self, id,sigla,descripcion,tipo_proyecto_cyt_id,tipo_proyecto_cyt_desc):
        self.id = id
        self.sigla = sigla
        self.descripcion = descripcion
        self.tipo_proyecto_cyt_id = tipo_proyecto_cyt_id
        self.tipo_proyecto_cyt_desc = tipo_proyecto_cyt_desc

class Ref_moneda:
    def __init__(self, moneda_id, descripcion,moneda_iso):
        self.moneda_id = moneda_id
        self.descripcion = descripcion
        self.moneda_iso = moneda_iso

class Ref_funcion:
    def __init__(self, funcion_id, descripcion):
        self.funcion_id = funcion_id
        self.descripcion = descripcion

class Ref_estadoProyecto:
    def __init__(self, estado_id, descripcion):
        self.estado_id = estado_id
        self.descripcion = descripcion

class Ref_disciplina:
    def __init__(self, disciplina_id,gran_area_codigo,gran_area_descripcion,area_codigo,area_descripcion,disciplina_codigo,disciplina_descripcion):
        self.disciplina_id = disciplina_id
        self.gran_area_codigo = gran_area_codigo
        self.gran_area_descripcion = gran_area_descripcion
        self.area_codigo = area_codigo
        self.area_descripcion = area_descripcion
        self.disciplina_codigo = disciplina_codigo
        self.disciplina_descripcion = disciplina_descripcion

class Nodo:
    def __init__(self,data):
        self.data=data
        self.next=None  # el siguiente vagon/nodo
    def __str__(self):
        return 'data: '+self.data  #siendo que self.data es una cadena. 


class listaenlazada: 
    def __init__(self):
        self.head=None # la locomotora. 

    def is_empty(self):
        return self.head is None # Devuelve un booleano, si es None, ta vacio. 
    
    def add_to_start(self,value):
        new_node=Nodo(value)
        new_node.next=self.head # Self.head es ahora el nuevo nodo. Osea el nuevo nodo pasa a ser la locomotora. 
        self.head=new_node

    def add_to_end(self, value):
        new_node = Nodo(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        
    def pop(self):   # borra el primer nodo, es pop x izquierda. 
        if self.is_empty(): # no hay nada q quitar
            return None
        popped_value=self.head.data # valor a devolver (quiero sacar el primer elemento. El pop en realidad saca el ultimo, este esta mal)
        self.head=self.head.next  # desvinculo. Hago que mi nueva locomotora sea el valor al que apuntaba mi locomotora anterior. 
        return popped_value
    
    def delete(self,value):  #elimina primer ocurrencia.  
        if self.is_empty(): # x si estacio, no puede borrar.
            return
        
        if self.head.data == value: # encuentra el primer vagon cuyo valor sea lo que quiero eliminar, lo desvinculo. (si atras hay otro igual no lo borra)
            self.head=self.head.next # desvinculo si es el primero. 
            return
        current=self.head
        while current.next: #mientras el siguiente vagon no sea None. 
            if current.next.data==value: 
                current.next=current.next.next # desvinculo
                return
            current=current.next

    def __str__(self):
        text=''
        current=self.head
        while current:
            text +=str(current.data) + '->'
            current=current.next
        text+='None'
        return text
    
    def __len__(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count

    def lista_por_inicio(self):#4
        proyectos_ordenados = self.sort_by_fecha_inicio()
        current = proyectos_ordenados.head
        while current:
            print(f"El ID del proyecto es: {current.data.proyecto_id}, la fecha de inicio es: {current.data.fecha_inicio}")
            current = current.next

    def sort_by_fecha_inicio(self):
        current = self.head
        while current:
            next_node = current.next
            while next_node:
                if current.data.fecha_inicio > next_node.data.fecha_inicio:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next
        return self

    def iterate(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
        

