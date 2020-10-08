# Displays a white window with a blue circle in the middle
import arcade
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Welcome to Arcade Snails"
background = None
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
# arcade.set_background_color(arcade.color.ALIZARIN_CRIMSON)

arcade.start_render()
# added background
background = arcade.load_texture("wow.jpg")
arcade.draw_lrwh_rectangle_textured(0, 0,SCREEN_WIDTH, SCREEN_HEIGHT,background)
# ended background

# Started making grid  



for y in range (100,700,100):
    # for horizontal line 
   
    arcade.draw_line(100,y,600,y,arcade.color.WHITE,5)
    # for verticle line
    arcade.draw_line(y,100,y,600,arcade.color.GRAY,5)


arcade.finish_render()

arcade.run()