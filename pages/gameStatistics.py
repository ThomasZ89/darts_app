
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

import copy

import logging
logging.basicConfig(level=logging.WARNING)

app_width = 590



def get_first_n_darts_avg(throws_dict, n):
    if len(throws_dict) < n:
        return 0
    score = 0
    for i in range(1,n+1):
        try:
            score += sum(throws_dict[i])
        except Exception:
            pass
    return round((score/n)*3,2)

def count_dart_throws(nested_dict):
    count_dict = copy.deepcopy(nested_dict)
    for key, item in count_dict.items():
        if item != [] and key != list(count_dict.keys())[-1]:
            while len(item) < 3:
                count_dict[key].append(0)
    return sum(len(value) for key, value in count_dict.items())

def get_checkout_ratio(throws_dict):
    values_list = []
    score = 101
    running_sum = 0
    check_outs = 0
    for key, values in throws_dict.items():
        for throw in values:
            if score-running_sum == 50 or (score-running_sum <= 40 and ((score-running_sum)%2==0)):
                check_outs += 1
            running_sum += throw
            if (running_sum+1) > score:
                running_sum -= sum(values)
            #print(check_outs,"---", score-running_sum,"---", throw)
    try:
        ratio = f"{round((1/check_outs),2)*100}%"
    except Exception:
        ratio = 0
    return ratio
    


        
def create_darts_user_display(user="", user_count=0, app_width=app_width,num_darts_value =0,
                              three_darts_avg_value=0, first_nine_darts_value=0, first_fifteen_darts_value=0, checkout_ratio_value=0):
    user = ft.Text(value=user, size=26, text_align=ft.alignment.center,
                   weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)

    num_darts = ft.Text(value=num_darts_value, size=16, text_align=ft.alignment.bottom_center,
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
        if user_count == 1:
            container_width = app_width
    except:
        pass
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
                height=45
        ),
            ft.Container(
                content=num_darts_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=30,
        ), ft.Container(
                content=three_darts_avg,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=60
        ),
            ft.Container(
                content=three_darts_avg_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=30,
        ),
            ft.Container(
                content=first_nine_darts,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=60
        ),
            ft.Container(
                content=first_nine_darts_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=30,
        ),
            ft.Container(
                content=first_fifteen_darts,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=60
        ),
            ft.Container(
                content=first_fifteen_darts_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=30,
        ),

            ft.Container(
                content=checkout_ratio,
                alignment=ft.alignment.bottom_center,
                bgcolor="#296251",
                width=container_width,
                height=60
        ),
            ft.Container(
                content=checkout_ratio_name,
                alignment=ft.alignment.center,
                bgcolor="#296251",
                width=container_width,
                height=30,
        ),


        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=0
    )




class gameStatistics(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page



    def go_to_home(self, e):
        self.page.session.clear()
        self.page.go('/')

    def build(self):

        users = self.page.session.get("users")
        user_count = len(users)
        darts_results = []
        for user in users:
            user_throws = self.page.session.get(f"{user}_throws")
            nine_darts_avg = get_first_n_darts_avg(throws_dict=user_throws,n=9)
            fifteen_darts_avg = get_first_n_darts_avg(throws_dict=user_throws,n=15)
            num_darts= count_dart_throws(user_throws)
            try:
                three_darts_avg = round(((self.page.session.get("base_score")/num_darts)*3),2)
            except Exception:
                three_darts_avg = 0
            checkout_ratio = get_checkout_ratio(user_throws)
            user_stats = create_darts_user_display(
                user=user,
                user_count=user_count,
                three_darts_avg_value = three_darts_avg,
                first_nine_darts_value = nine_darts_avg,
                first_fifteen_darts_value = fifteen_darts_avg,
                checkout_ratio_value = checkout_ratio,
                num_darts_value = num_darts,
                app_width=app_width)


            darts_results.append(user_stats)

        results_row= ft.Row(controls=darts_results, scroll=True)

        goBackBtn = ft.ElevatedButton(text='Go Back To Main Menu',
                    on_click= self.go_to_home,
                    style = ft.ButtonStyle(
                        color = ft.colors.GREEN,
                        bgcolor = ft.colors.WHITE,
                        side =  ft.BorderSide(1, ft.colors.BLACK)
                    ))

        go_back_row = ft.Row(controls= [goBackBtn])
        page_column = ft.Column(controls=[ results_row, go_back_row])


        return ft.Container(content=page_column, bgcolor="#3b8985", height=800)


