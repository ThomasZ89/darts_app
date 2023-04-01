from flet import *
from pages.home import Home
from pages.dartBoard import dartBoard
from pages.gameStatistics import gameStatistics

def views_handler(page):
  return {
    '/':View(
        route='/',
        controls=[
          Home(page)
        ]
      ),
    '/dartBoard':View(
        route='/dartBoard',
        controls=[
          dartBoard(page)
        ]
      ),
        '/gameStatistics':View(
        route='/gameStatistics',
        controls=[
          gameStatistics(page)
        ]
      ),
  }