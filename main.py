import arcade

arcade.open_window(1000, 900, "More Shapes")

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(50, 150, 200, 50, arcade.color.BITTER_LEMON )
arcade.draw_lrtb_rectangle_outline(160, 360, 150, 50, arcade.color.BRIGHT_UBE, 6)

arcade.draw_xywh_rectangle_outline(10, 10, 380, 250, arcade.color.EARTH_YELLOW, 6)
arcade.draw_xywh_rectangle_filled(405, 10, 150, 100, arcade.color.BLUE)

arcade.finish_render()
arcade.run()


