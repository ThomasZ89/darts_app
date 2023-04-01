from flet import *
from views import views_handler

def main(page: Page):

  def route_change(route):
    print(page.route)
    page.views.clear()
    page.views.append(
      views_handler(page)[page.route]
    )

  dart_throw_sound = Audio(src="sounds/dart_throw.mp3", autoplay=False)
  click_sound = Audio(src="sounds/key_sound.mp3", autoplay=False)
  delete_sound = Audio(src="sounds/delete_sound.mp3", autoplay=False)
  continue_sound = Audio(src="sounds/continue_sound.mp3", autoplay=False)
  page.overlay.append(dart_throw_sound)
  page.overlay.append(click_sound)
  page.overlay.append(delete_sound)
  page.overlay.append(continue_sound)
  page.on_route_change = route_change
  page.go('/')



app(target=main)