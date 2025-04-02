import flet as ft
import pyautogui
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

    posicao_cursor_planilha1 = (230, 199)
    posicao_cursor_planilha2 = (230, 199)
    posicao_cursor_filtro1_planilha1 = (88, 244)
    posicao_cursor_filtro2_planilha1 = (55, 483)
    posicao_cursor_filtro3_planilha1 = (175, 690)

    tempo1 = 0.5
    tempo2 = 0.5

    def automacao(e):
        qtd_linhas = int(quantidade_linhas.content.value)
        status_automacao2.content.value = "Em andamento!"
        status_automacao2.content.color = "#f0ed5a"
        page.update()
        
        pyautogui.hotkey("alt", "tab") #Altera para a planilha 2 e ajusta
        time.sleep(tempo2)
        pyautogui.press("esc")
        time.sleep(tempo1)
        pyautogui.hotkey("ctrl", "home")
        time.sleep(tempo1)

        pyautogui.keyDown("alt") #Altera para a planilha 1 e ajusta
        time.sleep(tempo2)
        pyautogui.press("tab")
        time.sleep(tempo2)
        pyautogui.press("tab")
        time.sleep(tempo2)
        pyautogui.keyUp("alt")
        time.sleep(tempo2)
        pyautogui.press("esc")
        time.sleep(tempo1)
        pyautogui.hotkey("ctrl", "home")
        time.sleep(tempo1)

        pyautogui.hotkey("alt", "tab") #Altera para a planilha 2
        time.sleep(tempo2)
        pyautogui.press("down")
        time.sleep(tempo1)
        
        linha = 0
        while linha < qtd_linhas:
            pyautogui.click(posicao_cursor_planilha2) # Pega o nome do produto
            time.sleep(tempo1)
            pyautogui.hotkey("ctrl", "a")
            time.sleep(tempo1)
            pyautogui.hotkey("ctrl", "c")
            time.sleep(tempo1)
            pyautogui.press("esc")
            time.sleep(tempo1)

            pyautogui.hotkey("alt", "tab") #Altera para a planilha 1, filtra e copia o status
            time.sleep(tempo2)
            pyautogui.press("esc")
            time.sleep(tempo1)
            pyautogui.click(posicao_cursor_filtro1_planilha1)
            time.sleep(tempo1)
            pyautogui.click(posicao_cursor_filtro2_planilha1)
            time.sleep(tempo1)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(tempo1)
            pyautogui.click(posicao_cursor_filtro3_planilha1)
            time.sleep(tempo1)
            pyautogui.press("down")
            time.sleep(tempo1)
            pyautogui.press("right")
            time.sleep(tempo1)
            pyautogui.press("right")
            time.sleep(tempo1)
            pyautogui.click(posicao_cursor_planilha1)
            time.sleep(tempo1)
            pyautogui.hotkey("ctrl", "a")
            time.sleep(tempo1)
            pyautogui.hotkey("ctrl", "c")
            time.sleep(tempo1)
            pyautogui.press("esc")
            time.sleep(tempo1)
            pyautogui.press("left")
            time.sleep(tempo1)
            pyautogui.press("left")
            time.sleep(tempo1)

            pyautogui.hotkey("alt", "tab") #Altera para a planilha 2, cola o valor e vai para o próximo
            time.sleep(tempo2)
            pyautogui.press("esc")
            time.sleep(tempo1)
            pyautogui.press("right")
            time.sleep(tempo1)
            pyautogui.hotkey("ctrl", "v")
            time.sleep(tempo1)
            pyautogui.press("left")
            time.sleep(tempo1)
            pyautogui.press("down")
            time.sleep(tempo1)

            linha += 1
        status_automacao2.content.value = "Finalizado!"
        status_automacao2.content.color = "#5DF065"
        page.update()
        pyautogui.keyDown("alt") #Altera para o programa
        time.sleep(tempo2)
        pyautogui.press("tab")
        time.sleep(tempo2)
        pyautogui.press("tab")
        time.sleep(tempo2)
        pyautogui.keyUp("alt")
        time.sleep(tempo2)

    quantidade_linhas = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START,
            cursor_color="#fffffe",
            cursor_width=2,
            selection_color="#5a93f0",
            text_size=18,
            label="Coloque a quantidade de Linhas",
            border_color="#fffffe",
            border_radius=15,
            border_width=2,
            width=350,
            height=50,
            text_style=ft.TextStyle(size=18, font_family=FONTE, color="#fffffe"),
            label_style=ft.TextStyle(size=20, font_family=FONTE, color="#fffffe", weight=ft.FontWeight.BOLD)
        )
    )

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
            value="Como usar:\n     1. Abra o arquivo excel: planilha1\n     2. Abra o arquivo excel: planilha2\n     3. Inicie essa automação (NESSA ORDEM)",
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
                quantidade_linhas,
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