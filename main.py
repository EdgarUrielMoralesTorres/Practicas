import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.padding = 20

    titulo = ft.Text(
        value="Registro de eventos",
        size=28,
        weight=ft.FontWeight.BOLD
    )

    nombreEve = ft.TextField(
        label="Nombre del evento",
        value="",
        hint_text="Escribe el nombre de tu evento"
    )

    tipoEven = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunion"),
        ],
        value="Conferencia",
        width=300
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial"
    )

    inscripcion = ft.Checkbox(
        label="Necesita inscripcion previa?",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1
    )

    resumen = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.BLUE
    )

    def mostrar_resumen(e):
        nombre = nombreEve.value.strip()

        if nombre == "":
            resumen.value = "Error: El nombre del evento no puede estar vacío."
            resumen.color = ft.Colors.RED
            page.update()
            return

        tipo = tipoEven.value
        mod = modalidad.value
        insc = inscripcion.value
        horas = duracion.value

        if insc == True:
            insc = "Necesita Inscripcion"
        else:
            insc = "No necesita Inscripcion"

        resumen.value = "El nombre del evento es: " + nombre
        resumen.value += "\nEs de tipo " + tipo
        resumen.value += "\nLa modalidad es " + mod
        resumen.value += "\nEste evento " + insc
        resumen.value += "\nEl evento dura un total de " + str(horas) + " horas"
        resumen.color = ft.Colors.BLACK
        page.update()

    boton = ft.Button(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen,
        bgcolor=ft.Colors.GREY,
        color=ft.Colors.BLACK
    )

    page.add(
        ft.Column(
            [
                titulo,
                nombreEve,
                tipoEven,
                modalidad,
                inscripcion,
                duracion,
                boton,
                ft.Divider(),
                resumen
            ],
            spacing=18
        )
    )

ft.app(target=main)
