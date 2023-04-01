
from turtle import width
import flet as ft
from flet import (
    Column,
    Container,
    ElevatedButton,
    Page,
    Row,
    Text,
    UserControl,
    border_radius,
    colors,
    TextField,
    AlertDialog
)






class User(UserControl):
    def __init__(self, name: str):
        self.name = name
        super().__init__()

    def select_user(self, e):
        self.controls[0].controls[0].content.selected = not self.controls[0].controls[0].content.selected
        self.controls[0].controls[0].content.update()
        #self.page.controls
        print("---")
        try:
            users = self.page.session.get("users")
            if users is None:
                users= []
        except:
            users= []
        if self.name in users:
            users.remove(self.name)
        else:
            users.append(self.name)
        self.page.session.set("users", users)

        if len(self.page.session.get("users")) > 0:
            pass
            #self.controls[0].content.controls[3].content.controls[0].disabled = False

        print(self.page.session.get("users"))
        

    def build(self):


        col1 = ft.IconButton(icon=ft.icons.PERSON, icon_color=ft.colors.BLACK, icon_size=70,
            selected_icon_color=ft.colors.AMBER_500,
            selected=False,
            style=ft.ButtonStyle(bgcolor  = {"selected": "#006400"}))
         
        cont1 = ft.Container(
                    content=col1,
                    alignment=ft.alignment.center,
                    width=200,
                    height=70,
                    on_click=self.select_user
                    #bgcolor=ft.colors.AMBER_500
                    )

        cont2 = ft.Container(
                    content=Text(self.name),
                    alignment=ft.alignment.center,
                    width=200,
                    height=30,
                    on_click=self.select_user
                    #bgcolor=ft.colors.AMBER_500,
                )
        return Column(controls=[cont1,cont2], horizontal_alignment=ft.alignment.center )

class Home(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        



    def create_new_user(self, board_name):
        user = User(board_name)
        self.users.controls.append(user)
        self.update()
             


    def add_user(self, e):
        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Cancel") or (type(e.control) is TextField and e.control.value != ""):
                self.create_new_user(dialog_text.value)
            dialog.open = False
            self.page.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = TextField(on_submit=close_dlg, on_change=textfield_change, border_color=ft.colors.BLACK)
        create_button = ElevatedButton(text="Confirm",color= ft.colors.BLACK, on_click=close_dlg, disabled=True)

        col = Column([
                dialog_text,
                Row([
                    ElevatedButton(
                        text="Cancel", on_click=close_dlg, color= ft.colors.BLACK),
                    create_button
                ], alignment="spaceBetween")
            ], tight=True)


        cont = Container(
            width=500,
            #bgcolor="#Fffffd",
            border_radius=border_radius.all(20),
            padding=2,
            content= col)

        dialog = AlertDialog(
            title=Text("New Username"),
            content=cont,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
            
        )

    

        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()




    def build(self):
        createUsrBtn = ft.FloatingActionButton(
                                content=ft.Row(
                                    [ft.Icon(ft.icons.ADD), ft.Text("Add user")], alignment="center", spacing=0
                                ),
                                bgcolor="#30874b",
                                shape=ft.RoundedRectangleBorder(radius=20),
                                width=110,
                                height=60,
                                mini=True,
                                on_click=self.add_user
                            )
        
        #userIconBtn = ft.IconButton(icon=ft.icons.PERSON, icon_color=ft.colors.BLACK, icon_size=70)
        
        self.users = ft.Row(wrap=True)

        goDartboardBtn = ft.ElevatedButton(text='Start the Game',
        on_click= lambda _: self.page.go('/dartBoard'),
        disabled=False,
        style = ft.ButtonStyle(
            color = ft.colors.BLACK,
            bgcolor="#30874b",
            side =  ft.BorderSide(1, ft.colors.BLACK)
        ))

        return   Container(
                    height=800, width=750,
                    bgcolor='green',
                    content=Column(
                        controls=[
                            Row(controls = [Text('Select the darts players', size=35)],alignment="center"),
                            Row(controls=[createUsrBtn], alignment="end"),
                            self.users,
                            Container(
                                content=Column(
                                    controls=[goDartboardBtn]
                                ), padding = 10
                            ),
                            
                        ]
                    )
                )
            
        
