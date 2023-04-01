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
)
#from regex import E
import copy

app_width = 590
game_score = 101


def fill_with_zeros(lst):
    while len(lst) < 3:
        lst.append(0)
    return lst

def count_dart_throws(nested_dict):
    count_dict = copy.deepcopy(nested_dict)
    for key, item in count_dict.items():
        if item != [] and key != list(count_dict.keys())[-1]:
            while len(item) < 3:
                count_dict[key].append(0)
    return sum(len(value) for key, value in count_dict.items())


def create_darts_results_display(user="", user_count=0, app_width=app_width,
                              three_darts_avg_value=0, first_nine_darts_value=0, first_fifteen_darts_value=0, checkout_ratio_value=0):
    user = ft.Text(value=user, size=26, text_align=ft.alignment.center,
                   weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    num_darts = ft.Text(value=22, size=16, text_align=ft.alignment.bottom_center,
                        weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    num_darts_name = ft.Text(value="Number of Darts", size=16, text_align=ft.alignment.center,
                             weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    three_darts_avg = ft.Text(value=three_darts_avg_value, size=16, text_align=ft.alignment.center,
                              weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    three_darts_avg_name = ft.Text(value="3-Darts AVG", size=16, text_align=ft.alignment.center,
                                   weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    first_nine_darts = ft.Text(value=first_nine_darts_value, size=16, text_align=ft.alignment.center,
                               weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    first_nine_darts_name = ft.Text(value="First 9 Darts AVG", size=16, text_align=ft.alignment.center,
                                    weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    first_fifteen_darts = ft.Text(value=first_fifteen_darts_value, size=16, text_align=ft.alignment.center,
                                  weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    first_fifteen_darts_name = ft.Text(value="First 15 Darts AVG", size=16, text_align=ft.alignment.center,
                                       weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    checkout_ratio = ft.Text(value=checkout_ratio_value, size=16, text_align=ft.alignment.center,
                             weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    checkout_ratio_name = ft.Text(value="Checkout Ratio", size=16, text_align=ft.alignment.center,
                                  weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    try:
        container_width = int((app_width-35)/user_count)
        container_width = max(container_width, 140)
    except:
        pass
    #container_width = 250
    return ft.Column(
        [ft.Container(
            content=user,
            alignment=ft.alignment.center,
            bgcolor="#296251",
            width=container_width,
            height=45,
            border=ft.border.only(bottom=ft.border.BorderSide(2, "white"))
        ),

            ft.Container(
                content=num_darts,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=35
        ),
            ft.Container(
                content=num_darts_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=25,
        ), ft.Container(
                content=three_darts_avg,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=40
        ),
            ft.Container(
                content=three_darts_avg_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=25
        ),
            ft.Container(
                content=first_nine_darts,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=40
        ),
            ft.Container(
                content=first_nine_darts_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=25
        ),
            ft.Container(
                content=first_fifteen_darts,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=40
        ),
            ft.Container(
                content=first_fifteen_darts_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=25
        ),

            ft.Container(
                content=checkout_ratio,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=40
        ),
            ft.Container(
                content=checkout_ratio_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=25
        ),


        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=0
    )

def create_darts_user_display(user = "", page="", user_count=0, app_width=app_width):
        score = ft.Text(value= page.session.get(user+"_score"),
        size=60, text_align= ft.alignment.center, weight=ft.FontWeight.W_700, color=ft.colors.WHITE)
        user_name = ft.Text(value=user, size=22, text_align= ft.alignment.center, weight=ft.FontWeight.W_600, color=ft.colors.WHITE)
        user_average = ft.Text(value=0, size=17, text_align= ft.alignment.center, weight=ft.FontWeight.W_100, color=ft.colors.WHITE)
        try:
            container_width = int((app_width-35)/user_count)
            container_width = max(container_width,140)
        except:
            pass
        #container_width = 250
        return ft.Column(
            [
                ft.Container(
                    content=score,
                    alignment=ft.alignment.bottom_center,
                    bgcolor="#232e5c",
                    width=container_width,
                    height=90
                ),
                ft.Container(
                    content=user_name,
                    alignment=ft.alignment.top_center,
                    bgcolor="#232e5c",
                    width=container_width,
                    height=32
                ),
                ft.Container(
                    content=user_average,
                    alignment=ft.alignment.center,
                    bgcolor="#296251",
                    width=container_width,
                    height=25
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=0
        )

test = create_darts_results_display(
            user="a", user_count=3, app_width=app_width)

winAlert = ft.AlertDialog(
        modal=True,
        title=ft.Text("Game is over"),
        content=test,
        actions=[
            ft.TextButton("Go back to Main menu")
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

class dartBoard(UserControl):
    def __init__(self,page):
        super().__init__()
        self.page = page
        userlist = []
        users = self.page.session.get("users")
        if users is None:
            users= []
        for user in users:
            userlist.append(create_darts_user_display(user=user, page=page, user_count=len(users),app_width=app_width))
        
        

        user_row= ft.Row(controls=userlist, scroll=True, auto_scroll=True)
        self.page.add(user_row)
        self.page.update()

    def createBtn(self, value):
        return ft.ElevatedButton(
        content=ft.Row([ ft.Text(value=str(value), size=20)], alignment="center"),
        style=ft.ButtonStyle(
            color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
            bgcolor={ft.MaterialState.DEFAULT: ft.colors.GREEN_800},
            overlay_color=ft.colors.TRANSPARENT,
            side={ft.MaterialState.DEFAULT: ft.BorderSide(
                2, ft.colors.BLACK)},
            shape={
                ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=2)}
        ), width=110, height=80, data=value, on_click=self.button_clicked)

    def createDblBtn(self):
        return ft.ElevatedButton(
        content=ft.Row([ ft.Text(value="Double", size=20)], alignment="center"),
        style=ft.ButtonStyle(
            color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
            bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200,
                    "": ft.colors.GREEN_800},
            padding={ft.MaterialState.DEFAULT: 10},
            overlay_color=ft.colors.TRANSPARENT,
            side={ft.MaterialState.DEFAULT: ft.BorderSide(
                2, ft.colors.BLACK)},
            shape={
                ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=2)}
        ), width=276, height=90, on_click=self.double_values)    


    def createTrplBtn(self):
            return ft.ElevatedButton(
            content=ft.Row([ ft.Text(value="Triple", size=20)], alignment="center"),
            style=ft.ButtonStyle(
                color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
                bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200,
                        "": ft.colors.GREEN_800},
                padding={ft.MaterialState.DEFAULT: 1},
                overlay_color=ft.colors.TRANSPARENT,
                side={ft.MaterialState.DEFAULT: ft.BorderSide(
                    2, ft.colors.BLACK)},
                shape={
                    ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=2)}
            ), width=276, height=90, on_click=self.triple_values) 
    
    def createDeletelBtn(self):
            return ft.ElevatedButton(
            content=ft.Row([ ft.Text(value="Del", size=20)], alignment="center"),
            style=ft.ButtonStyle(
                color={ft.MaterialState.DEFAULT: ft.colors.BLACK},
                bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200,
                        "": ft.colors.GREEN_800},
                padding={ft.MaterialState.DEFAULT: 10},
                overlay_color=ft.colors.TRANSPARENT,
                side={ft.MaterialState.DEFAULT: ft.BorderSide(
                    2, ft.colors.BLACK)},
                shape={
                    ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=2)}
            ), width=110, height=160, on_click=self.delete_last_throw) 


    def build(self):
        self.oneBtn=self.createBtn(value=1)
        self.twoBtn=self.createBtn(value=2)
        self.threeBtn=self.createBtn(value=3)
        self.fourBtn=self.createBtn(value=4)
        self.fiveBtn=self.createBtn(value=5)
        self.sixBtn=self.createBtn(value=6)
        self.sevenBtn=self.createBtn(value=7)
        self.eightBtn=self.createBtn(value=8)
        self.nineBtn=self.createBtn(value=9)
        self.tenBtn=self.createBtn(value=10)
        self.elevenBtn=self.createBtn(value=11)
        self.twelveBtn=self.createBtn(value=12)
        self.thirteenBtn=self.createBtn(value=13)
        self.fourteenBtn=self.createBtn(value=14)
        self.fifteenBtn=self.createBtn(value=15)
        self.sixteenBtn=self.createBtn(value=16)
        self.seventeenBtn=self.createBtn(value=17)
        self.eighteenBtn=self.createBtn(value=18)
        self.nineteenBtn=self.createBtn(value=19)
        self.twentyBtn=self.createBtn(value=20)

        self.zeroBtn=self.createBtn(value=0)
        self.twentyfiveBtn=self.createBtn(value=25) 
        self.fiftyBtn=self.createBtn(value=50)

        self.BtnNames = ['oneBtn', 'twoBtn', 'threeBtn', 'fourBtn', 'fiveBtn', 'sixBtn', 'sevenBtn', 'eightBtn',
                    'nineBtn', 'tenBtn', 'elevenBtn', 'twelveBtn', 'thirteenBtn', 'fourteenBtn', 'fifteenBtn',
                    'sixteenBtn', 'seventeenBtn', 'eighteenBtn', 'nineteenBtn', 'twentyBtn']

        self.DblBtn=self.createDblBtn()
        self.TrplBtn=self.createTrplBtn()
        self.DeleteBtn= self.createDeletelBtn()
        
        self.dartOne  =   ft.TextField(disabled=True, value="Dart 1",color=ft.colors.WHITE, width=155, text_align="CENTER")
        self.dartTwo  =   ft.TextField(disabled=True, value="Dart 2",color=ft.colors.WHITE, width=155, text_align="CENTER")
        self.dartThree =  ft.TextField(disabled=True, value="Dart 3",color=ft.colors.WHITE, width=155, text_align="CENTER")
        
        # Name of the Dartsfields
        self.dartFields = {"dartOne":"Dart 1","dartTwo": "Dart 2","dartThree": "Dart 3"}


        self.scoreBtn = ft.ElevatedButton(content=ft.Text(value="120 Points", size=35),
                                 height=200,width=140,
                                 style=ft.ButtonStyle(shape=ft.CircleBorder()
                                                      ),
                                 )

        self.goBackBtn = ft.ElevatedButton(content=ft.Text(value="Go Back", size=25),
                                  bgcolor=ft.colors.RED, color=ft.colors.BLACK, on_click=self.close_bs_go_back,
                                  height=140, width=110, style=ft.ButtonStyle(
                                shape={
                                    ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=0)}
                                    ))

        self.continueBtn = ft.ElevatedButton(content=ft.Text(value="Continue", size=25),
                                    bgcolor=ft.colors.GREEN, color=ft.colors.BLACK,
                                    height=140, width=450, on_click=self.close_bs_continue,
                                    style=ft.ButtonStyle(
                                shape={
                                    ft.MaterialState.DEFAULT: ft.CountinuosRectangleBorder(radius=0)}
                            )
                            )

        self.bottomSheet = ft.AlertDialog(
        content=ft.Container(
            ft.Column(controls=[self.scoreBtn,
                                ],
                      horizontal_alignment="CENTER",
                      alignment="END",
                      spacing=120
                      ), 
        padding=0,
        width=590,
        height=250,
        bgcolor=ft.colors.TRANSPARENT
        ),
        actions=[ft.Row(controls=[self.goBackBtn,
                                                 self.continueBtn], spacing=0
                                       )],
        open=False,
        modal=True,
        content_padding=0,
        shape = ft.CountinuosRectangleBorder(radius=0),
        actions_padding=0
    )
        

        test = create_darts_results_display(
            user="a", user_count=3, app_width=app_width)
        
        self.winAlert = winAlert


        # self.winAlert = ft.AlertDialog(
        #     modal=True,
        #     title=ft.Text("Game is over"),
        #     content=test,
        #     actions=[
        #         ft.TextButton("Go back to Main menu", on_click=self.end_round)
        #     ],
        #     actions_alignment=ft.MainAxisAlignment.END
        # )


        self.userlist = []
        users = self.page.session.get("users")
        if users is None:
            users= []
           
        
        for user in users:
            self.page.session.set(user+"_throws",{1:[]})
            self.page.session.set(user+"_throws_valid",{1:[]})
            self.page.session.set(user+"_score",game_score)
            self.userlist.append(create_darts_user_display(user=user, page=self.page, user_count=len(users),app_width=app_width))
        
        self.page.session.set("base_score",game_score)

        user_row= ft.Row(controls=self.userlist, scroll=True)
        self.page.session.set("active_user_index", 0)


        return Container(
            width=app_width,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=Column(
                controls=[user_row,
                        Row(controls=[self.dartOne, self.dartTwo, self.dartThree], spacing=5, alignment=ft.MainAxisAlignment.SPACE_AROUND),
                        Row(width=750,
                            controls=[
                                Column(controls=[self.oneBtn,self.fiveBtn ], spacing=1),
                                Column(controls=[self.twoBtn,self.sixBtn ], spacing=1),
                                Column(controls=[self.threeBtn,self.sevenBtn ], spacing=1),
                                Column(controls=[self.fourBtn,self.eightBtn ], spacing=1),
                                Column(controls=[self.DeleteBtn], spacing=1)
                                ], spacing=1),
                        Row(controls=[self.nineBtn, self.tenBtn, self.elevenBtn, self.twelveBtn, self.zeroBtn], spacing=1),
                        Row(controls=[self.thirteenBtn, self.fourteenBtn, self.fifteenBtn, self.sixteenBtn, self.twentyfiveBtn], spacing=1),
                        Row(controls=[self.seventeenBtn, self.eighteenBtn, self.nineteenBtn, self.twentyBtn, self.fiftyBtn], spacing=1),
                        Row(controls=[self.DblBtn, self.TrplBtn], spacing=1),
                        Column(controls=[self.bottomSheet]),
                        Column(controls=[self.winAlert])
                        ], spacing=1
                        )
                        
                        )                      
    
    def clear_dart_fields(self, e):
        for dartsfield_name in list(self.dartFields.keys())[::-1]:
            self.dartsfield = getattr(self, dartsfield_name)
            self.dartsfield.value = self.dartFields[dartsfield_name]
        self.update()

    def close_bs_go_back(self, e):
        self.bottomSheet.open = False
        self.delete_last_throw(self)
        self.bottomSheet.update()
    
    
    def close_bs_continue(self, e):
        self.page.overlay[3].volume = 1
        self.page.overlay[3].play()
        self.page.overlay[3].volume = 0
        user = self.controls[0].content._get_children()[0].controls[0].controls[1].content.value
        base_score = self.page.session.get("base_score")
        active_throws = e.page.session.get(f"{user}_throws")
        valid_throws = e.page.session.get(f"{user}_throws_valid")
        valid_throw_sum = sum(active_throws[i][j] for i in valid_throws.keys() for j in range(len(valid_throws[i])) if valid_throws[i][j])
        new_score = base_score-valid_throw_sum
        if new_score == 0:
             self.page.go('/gameStatistics')
        else:
            self.bottomSheet.open = False
            # Change User order
            first_user = self.controls[0].content._get_children()[0].controls.pop(0)
            self.controls[0].content._get_children()[0].controls.append(first_user )
            
            self.clear_dart_fields(self)
            self.update()
            self.bottomSheet.update()

    def delete_last_throw(self, e):
        # Play sound
        self.page.overlay[2].volume = 1
        self.page.overlay[2].play()
        self.page.overlay[2].volume = 0
        # Reset value of Darts field
        for dartsfield_name in list(self.dartFields.keys())[::-1]:
            self.dartsfield = getattr(self, dartsfield_name)
            if self.dartsfield.value not in list(self.dartFields.values()): 
                self.dartsfield.value = self.dartFields[dartsfield_name]
                self.update()
                break

        # Remove last throw from list
        active_user = self.controls[0].content._get_children()[0].controls[0].controls[1].content.value
        active_throws = e.page.session.get(active_user+"_throws")
        valid_throws = e.page.session.get(active_user+"_throws_valid")
        current_throws_key = list(active_throws)[-1]
        
        print("before delete", "------",active_throws)
        is_round_end_back = len(active_throws[current_throws_key]) == 0

        if len(active_throws[current_throws_key]) == 0:
            active_throws.pop(current_throws_key)
            valid_throws.pop(current_throws_key)
            current_throws_key -= 1

        active_throws[current_throws_key].pop()
        valid_throws[current_throws_key].pop()
        #Set all throws in this Aufnahme to True again
        valid_throws[current_throws_key] = [True for i in valid_throws[current_throws_key]]
        e.page.session.set(active_user+"_throws",active_throws)

        base_score = self.page.session.get("base_score")
        new_score = base_score - sum([active_throws[i][j] for i in valid_throws.keys() for j in range(len(valid_throws[i])) if valid_throws[i][j]])
        self.userlist[0].controls[0].content.value = new_score

        print("after delete", "------",active_throws)

        self.update_average(e=e)
        self.update()


    def is_throw_valid(self, throws, valid_throws, last_throw, score, multiplier):
        # calculate the sum of all valid throws
        valid_throw_sum = sum([throws[i][j] for i in valid_throws.keys() for j in range(len(valid_throws[i])) if valid_throws[i][j]])
        # check if the last throw is valid based on the score and sum of valid throws
        if last_throw == (score - valid_throw_sum) and last_throw ==50:
            return True
        if last_throw == (score - valid_throw_sum) and multiplier == "double":
            return True
        if last_throw >= (score - valid_throw_sum-1):
            return False
        else:
            return True

    def calculate_turn(self, e, throw_value):
        user = self.controls[0].content._get_children()[0].controls[0].controls[1].content.value
        base_score = self.page.session.get("base_score")
        multiplier = e.page.session.get("muliplier")
        valid_throws = e.page.session.get(f"{user}_throws_valid")
        active_throws = e.page.session.get(f"{user}_throws")
        current_throws_key = list(active_throws)[-1]

        is_valid = self.is_throw_valid(throws=active_throws, valid_throws=valid_throws, last_throw=throw_value, score=base_score, multiplier=multiplier)
        if not is_valid:
            valid_throws[current_throws_key].append(is_valid)
            valid_throws[current_throws_key] = [False for _ in valid_throws[current_throws_key]]

            active_throws[current_throws_key].append(throw_value)
            valid_throws[current_throws_key+1]= []
            active_throws[current_throws_key+1]= []
            round_score = 0
        else:        
            valid_throws[current_throws_key].append(is_valid)
            active_throws[current_throws_key].append(throw_value)
            round_score = sum(active_throws[current_throws_key])
            if len(active_throws[current_throws_key]) == 3:
                current_throws_key +=1
                valid_throws[current_throws_key] = []
                active_throws[current_throws_key] = []

        e.page.session.set(f"{user}_throws", active_throws)
        valid_throw_sum = sum(active_throws[i][j] for i in valid_throws.keys() for j in range(len(valid_throws[i])) if valid_throws[i][j])

        new_score = base_score - valid_throw_sum

        e.page.session.set(f"{user}_score", new_score)

        self.userlist[0].controls[0].content.value = new_score
        self.update()
        print(valid_throws)
        print(active_throws)
        return is_valid, round_score, 
    
    def update_average(self, e):
        user = self.controls[0].content._get_children()[0].controls[0].controls[1].content.value
        try:
            active_throws = e.page.session.get(f"{user}_throws")
            valid_throws = e.page.session.get(f"{user}_throws_valid")
            valid_throw_sum = sum(active_throws[i][j] for i in valid_throws.keys() for j in range(len(valid_throws[i])) if valid_throws[i][j])

            throws_count= count_dart_throws(active_throws.copy())
            avg = (
                (valid_throw_sum*3)/
                float(throws_count)
                )
        except Exception:
            avg = 0
        avg = round(avg,2)
        self.userlist[0].controls[2].content.value = avg
        self.update()


    def button_clicked(self, e):
        #Play darts audio
        self.page.overlay[0].volume = 1
        self.page.overlay[0].play()
        self.page.overlay[0].volume = 0
        data = e.control.data
        # Change value, for first textfield with default value
        for dartsfield_name in self.dartFields.keys():
            self.dartsfield = getattr(self, dartsfield_name)
            if self.dartsfield.value in list(self.dartFields.values()):
                self.dartsfield.value = data   
                break
        
        is_valid, valid_throw_sum = self.calculate_turn(e=e, throw_value=e.control.data)
        self.update_average(e=e)

        if not is_valid:
            self.bottomSheet.open = True
            self.page.theme = ft.theme.Theme(color_scheme_seed="red")
            self.page.update()
            self.bottomSheet.content.content.controls[0].content.value = 0
            self.bottomSheet.update()
            self.page.update()
        
        if dartsfield_name =="dartThree":
            if is_valid:
                self.page.theme = ft.theme.Theme(color_scheme_seed="green")
            self.page.update()
            self.bottomSheet.open = True
            self.bottomSheet.content.content.controls[0].content.value = valid_throw_sum
            self.bottomSheet.update()
        
        user = self.controls[0].content._get_children()[0].controls[0].controls[1].content.value
        base_score = self.page.session.get("base_score")
        active_throws = e.page.session.get(f"{user}_throws")
        valid_throws = e.page.session.get(f"{user}_throws_valid")
        valid_throw_sum = sum(active_throws[i][j] for i in valid_throws.keys() for j in range(len(valid_throws[i])) if valid_throws[i][j])
        new_score = base_score-valid_throw_sum
        if new_score == 0:
            if is_valid:
                self.page.theme = ft.theme.Theme(color_scheme_seed="green")
            self.page.update()
            self.bottomSheet.open = True
            self.bottomSheet.content.content.controls[0].content.value = valid_throw_sum
            self.bottomSheet.update()

        
        self.update()
    
    def double_values(self, e):
        self.page.overlay[1].volume = 1
        self.page.overlay[1].play()
        self.page.overlay[1].volume = 0
        if str(getattr(self, self.BtnNames[0]).content.controls[0].value)[0:2] == "T ":
            self.triple_values(e = e)
        for btn_name in self.BtnNames:
            self.button = getattr(self, btn_name)
            if str(self.button.content.controls[0].value)[0:2] == "D ":
                e.page.session.set("muliplier","none")
                self.button.data = int(self.button.data/2)
                self.button.content.controls[0].value = self.button.content.controls[0].value[2:]
            else:
                self.button.data = int(self.button.data*2)
                e.page.session.set("muliplier","double")
                self.button.content.controls[0].value = "D "+str(self.button.content.controls[0].value)
        self.update()
    

    def triple_values(self, e):
        self.page.overlay[1].volume = 1
        self.page.overlay[1].play()
        self.page.overlay[1].volume = 0
        if str(getattr(self, self.BtnNames[0]).content.controls[0].value)[0:2] == "D ":
            self.double_values(e = e)
        for btn_name in self.BtnNames:
            self.button = getattr(self, btn_name)
            if self.button.content.controls[0].value[0:2] == "T ":
                e.page.session.set("muliplier","none")
                self.button.data = int(self.button.data/3)
                self.button.content.controls[0].value = self.button.content.controls[0].value[2:]
            else:
                self.button.data = int(self.button.data*3)
                e.page.session.set("muliplier","triple")
                self.button.content.controls[0].value = "T "+self.button.content.controls[0].value
        self.update()

