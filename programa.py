import flet as ft
import pyautogui
import pyperclip
import time

FONTE = "JetBrains Mono"

def tela(page: ft.Page):
    
    page.title = "Automação."
    page.bgcolor = "#16161a"
    page.window.width= 640
    page.window.height = 360
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.alignment = ft.alignment.center
    page.padding = 10
    page.window.center()

    posicao_excel = (227, 198)
    posicao_entrada_produto = (34, 454)

    def automacao(e): 
        status_automacao2.content.value = "Em andamento!"
        status_automacao2.content.color = "#f0ed5a"
        pyperclip.copy("")
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)

        pyautogui.press("down")
        time.sleep(1)
        pyautogui.click(posicao_excel)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(1)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)

        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")
        time.sleep(1)

        pyautogui.click(posicao_entrada_produto)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)

    botao_iniciar = ft.Container(
        content=ft.Text(
            value="Iniciar Automação",
            text_align=ft.TextAlign.CENTER,
            font_family=FONTE,
            size=20,
            weight=ft.FontWeight.BOLD,
            color="#fffffe"
        ),
        alignment=ft.alignment.center,
        width=300,
        height=30,
        bgcolor="#7f5af0",
        border_radius=10,
        on_click=automacao
    )

    tutorial_automacao = ft.Container(
        content=ft.Text(
            value="Como usar:\n     1. Abra o programa desejado\n     2. Abra o arquivo excel\n     3. Inicie essa automação (NESSA ORDEM)",
            text_align=ft.TextAlign.START,
            font_family=FONTE,
            size=14,
            weight=ft.FontWeight.BOLD,
            color="#fffffe"
        ),
        alignment=ft.alignment.center
    )

    status_automacao1 = ft.Container(
        content=ft.Text(
            value="Status: ",
            text_align=ft.TextAlign.START,
            font_family=FONTE,
            size=20,
            weight=ft.FontWeight.BOLD,
            color="#fffffe"
        ),
        alignment=ft.alignment.center
    )

    status_automacao2 = ft.Container(
        content=ft.Text(
            value="Precisa ser iniciado!",
            text_align=ft.TextAlign.START,
            font_family=FONTE,
            size=20,
            weight=ft.FontWeight.BOLD,
            color="#5a93f0"
        ),
        alignment=ft.alignment.center
    )

    linha_status_automacao = ft.Container(
        ft.Row(
            [
                status_automacao1,
                status_automacao2
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    tela_geral = ft.Container(
        ft.Column(
            [
                botao_iniciar,
                tutorial_automacao,
                linha_status_automacao
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_geral)

ft.app(target=tela)