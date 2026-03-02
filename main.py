import flet as ft

def main(page: ft.Page):
    page.title = "Monto final"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    texto = ft.Text("de ingresar el monto a pagar")

    resultado = ft.Text("Tu propina es de 0")
    resultado2 = ft.Text("Tu monto a pagar es de 0")

    def calcular(e):
        try:
            monto = float(CanIn.value)
        except:
            monto=0
        porcentaje = Cal.value
        propina = monto * porcentaje
        Mon = monto + propina
        resultado.value = f"Tu propina es de {propina}"
        resultado2.value = f"Tu Monto a final a pagarr es de {Mon}"
        page.update()    
    CanIn = ft.TextField(value="0", width=100, on_change=calcular)
    Cal = ft.Slider( min=0.05, max=0.45, divisions=8,value=0.05, on_change=calcular )

    page.add(
        ft.Column([
                ft.Row([texto, CanIn], alignment=ft.MainAxisAlignment.CENTER),
                Cal,
                resultado,
                resultado2
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ))

ft.app(target=main)