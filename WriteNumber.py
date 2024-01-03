import flet as ft
import inflect 

pl = inflect.engine()

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100, color="white")
    word_number = ft.Text(value="zero", text_align=ft.TextAlign.CENTER, width=250, color="white")
    word_number.disabled = True
    txt_number.disabled = True

    #Subtrair 1
    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        word_number.value = pl.number_to_words(txt_number.value)
        page.update()

    #Somar 1
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        word_number.value = pl.number_to_words(txt_number.value)
        page.update()

    #Subtrair 10
    def minus_click_10(e):
        txt_number.value = str(int(txt_number.value) - 10)
        word_number.value = pl.number_to_words(txt_number.value)
        page.update()

    #Somar 10
    def plus_click_10(e):
        txt_number.value = str(int(txt_number.value) + 10)
        word_number.value = pl.number_to_words(txt_number.value)
        page.update()

    #Subtrair 100
    def minus_click_100(e):
        txt_number.value = str(int(txt_number.value) - 100)
        word_number.value = pl.number_to_words(txt_number.value)
        page.update()

    #Somar 100
    def plus_click_100(e):
        txt_number.value = str(int(txt_number.value) + 100)
        word_number.value = pl.number_to_words(txt_number.value)
        page.update()

    

    page.add(
        ft.Row(
            [
                ft.ElevatedButton("-100", on_click=minus_click_100),
                ft.ElevatedButton("-10", on_click=minus_click_10),
                ft.ElevatedButton("-1", on_click=minus_click),
                txt_number,
                ft.ElevatedButton("+1", on_click=plus_click),
                ft.ElevatedButton("+10", on_click=plus_click_10),
                ft.ElevatedButton("+100", on_click=plus_click_100),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                word_number
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)