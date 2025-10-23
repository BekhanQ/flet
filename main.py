import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'My first programm'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text= ft.Text('Hello World!')
    greeting_history = []
    history_text = ft.Text('greeting history')

    # def update_history():
    #     history_controls = [ft.Text("greeting history:")]


    def on_button_click(_):
        # print(name_input.value)
        name = name_input.value.strip()
        print(name)

        if name:
            print(greeting_text)
            greeting_text.value = f'Hello {name}'
            print(greeting_text)
            name_input.value = ''

            timestemp = datetime.now().strftime('%M:%S')
            greeting_history.append(f'{timestemp} - {name}')
            history_text.value = 'greeting history:\n'+'\n'.join(greeting_history)


        else:
            print('nothing has entered!')
            greeting_text.value = 'please enter name'
        page.update()

    name_input = ft.TextField(label='enter name:', on_submit=on_button_click)
    name_button = ft.ElevatedButton('send', on_click=on_button_click)
    
    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'greeting history:'
        page.update()
    
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    # page.add(greeting_text, name_input, name_button, history_text)

    page.add(greeting_text, name_input,
             ft.Row([name_button,clear_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
             ft.Row([history_text], alignment=ft.MainAxisAlignment.START)
             )
             

ft.app(target=main)