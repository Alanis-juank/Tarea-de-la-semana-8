# Dashboard.
class Tarea:
    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def mostrar_tarea(self):
        print(f"Tarea: {self.titulo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Estado: {self.estado}")
        print("-" * 30)


class Dashboard:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print("✅ Tarea agregada correctamente")

    def mostrar_tareas(self):
        print("\n📌 DASHBOARD - TAREAS DE POO")
        for tarea in self.tareas:
            tarea.mostrar_tarea()


# Programa principal
if __name__ == "__main__":
    dashboard = Dashboard()

    tarea1 = Tarea(
        "Tarea POO",
        "Implementar clases, objetos y herencia en Python",
        "Pendiente"
    )

    tarea2 = Tarea(
        "Foro Académico",
        "Participar en el foro sobre POO",
        "Completada"
    )

    dashboard.agregar_tarea(tarea1)
    dashboard.agregar_tarea(tarea2)

    dashboard.mostrar_tareas()
