# -*- coding: utf-8 -*-
"""
This uses Pillow (PIL compatible alternative) to generate
the template I use for Chinese Character practice.

Oisin Mulvihill
2018-01-28
"""
from PIL import Image, ImageDraw

SCREEN = (1404, 1872)  # Resolution of my reMarkable device
BLACK, GRAY, WHITE = ((col, )*3 for col in (50, 200, 255))


def hanzi_box(draw, top, left, width):
    """Generate a black box and then draw the guide lines in gray."""
    draw.rectangle([(top, left), (top + width, left + width)], outline=BLACK, fill=WHITE)
    draw.line([(top, left), (top + width, left + width)], fill=GRAY)  # line 1
    draw.line([(top, left + (width / 2)), (top + width, left + (width / 2))], fill=GRAY)  # line 2
    draw.line([(top, left + width), (top + width, left)], fill=GRAY)  # line 3
    draw.line([(top + (width / 2), left), (top + (width / 2), left + width)], fill=GRAY)  # line 4


def main(debug=False):
    """All sizes here are in pixels."""
    # The raw PNG image will take up the whole screen on my reMarkable device:
    im = Image.new('RGBA', SCREEN, (0, 255, 0, 0))
    draw = ImageDraw.Draw(im)

    UI_MENU_PAD_TOP, UI_MENU_PAD_LEFT, BOX_PAD, HANZI_BOX_WIDTH = 185, 135, 30, 100
    print(f"screen: {SCREEN} padding: {(UI_MENU_PAD_TOP, UI_MENU_PAD_LEFT)} hanzi box width: {HANZI_BOX_WIDTH}")

    # Account of UI menus and work out the "drawable" area I will put boxes into:
    s_top, s_left = (UI_MENU_PAD_TOP, UI_MENU_PAD_LEFT)
    top_min, left_min = (s_top, s_left)
    top_max, left_max = (SCREEN[0], SCREEN[1])
    draw_area_width = left_max - left_min
    draw_area_height = top_max - top_min
    print(f"draw_area_width: {draw_area_width} draw_area_height: {draw_area_height}")

    # Work out the amount of box rows and columns I can fit in the "drawable" area.
    box_columns = draw_area_width // (HANZI_BOX_WIDTH + BOX_PAD)
    box_rows = draw_area_height // (HANZI_BOX_WIDTH + BOX_PAD)
    print(f"box rows: {box_rows} columns: {box_columns}")

    # Generate:
    for row in range(box_rows):
        for col in range(box_columns):
            top = (s_top + (row * HANZI_BOX_WIDTH) + (row * BOX_PAD))
            left = (s_left + (col * HANZI_BOX_WIDTH) + (col * BOX_PAD))
            hanzi_box(draw, top, left, HANZI_BOX_WIDTH)

    if debug:
        im.show()
    else:
        with open('static/output/hanzi_grid.png', 'wb') as fd:
            im.save(fd, "PNG")


if __name__ == "__main__":
    main()
