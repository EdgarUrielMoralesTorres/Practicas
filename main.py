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

    fecha_evento = ft.Text("Fecha no seleccionada")

    def selFech(e):
        if tiem.value:
            fecha_evento.value = "Fecha seleccionada: " + tiem.value.strftime("%d/%m/%Y")
            page.update()

    tiem = ft.DatePicker(on_change=selFech)

    page.overlay.append(tiem)

    def abriFech(e):
        tiem.open = True
        page.update()

    boton_fecha = ft.Button(
        content=ft.Text("Seleccionar fecha"),
        on_click=abriFech
    )

    resumen = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.W_500
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

        if insc:
            texto_insc = "Necesita inscripción"
        else:
            texto_insc = "No necesita inscripción"

        resumen.value = "El nombre del evento es: " + nombre
        resumen.value += "\nEs de tipo " + tipo
        resumen.value += "\nLa modalidad es " + mod
        resumen.value += "\nEste evento " + texto_insc
        resumen.value += "\nEl evento dura " + str(horas) + " horas"
        resumen.value += "\n" + fecha_evento.value

        resumen.color = ft.Colors.BLACK
        page.update()

    boton = ft.Button(
        content=ft.Text("Mostrar resumen"),
        on_click=mostrar_resumen
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
                boton_fecha,
                fecha_evento,
                boton,
                ft.Divider(),
                resumen
            ],
            spacing=18
        )
    )

ft.run(main)
