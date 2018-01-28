# -*- coding: utf-8 -*-
"""
This uses Pillow (PIL compatible alternative) to generate the template I use
for Chinese Character practice.

Oisin Mulvihill
2018-01-28

"""
from PIL import Image, ImageDraw

# Resolution of my reMarkable device:
SCREEN = (1404, 1872)
BLACK = (50, 50, 50)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)


def hanzi_box(draw, top, left, width):
    """Generate a black box and then draw the guide lines in gray."""
    draw.rectangle(
        [
            (top, left),
            (top + width, left + width)
        ],
        outline=BLACK,
        fill=WHITE,
    )

    # line 1:
    draw.line([(top, left), (top + width, left + width)], fill=GRAY)

    # line 2:
    draw.line(
        [(top, left + (width / 2)), (top + width, left + (width / 2))],
        fill=GRAY
    )

    # line 3:
    draw.line(
        [(top, left + width), (top + width, left)],
        fill=GRAY
    )

    # line 4:
    draw.line(
        [(top + (width / 2), left), (top + (width / 2), left + width)],
        fill=GRAY
    )


def main():
    """All sizes here are in pixels.

    """
    # The raw PNG image will take up the whole screen on my reMarkable device:
    im = Image.new('RGBA', SCREEN, (0, 255, 0, 0))
    draw = ImageDraw.Draw(im)

    # Worked out by eye mainly:
    UI_MENU_PAD = 135

    # A box size and box spacing I feel comfortable after trial an error:
    BOX_PAD = 30
    HANZI_BOX_WIDTH = 100
    print "screen: {} padding: {} hanzi box width: {}".format(
        SCREEN, UI_MENU_PAD, HANZI_BOX_WIDTH
    )

    # Account of UI menus and work out the "drawable" area I will put
    # boxes into:
    s_top, s_left = (0 + UI_MENU_PAD, 0 + UI_MENU_PAD)
    top_min, left_min = (s_top, s_left)
    top_max, left_max = (SCREEN[0], SCREEN[1])
    draw_area_width = left_max - left_min
    draw_area_height = top_max - top_min
    print "draw_area_width: {} draw_area_height: {}".format(
        draw_area_width, draw_area_height
    )

    # Work out the amount of box rows and columns I can fit in the
    # "drawble" area.
    box_columns = draw_area_width / (HANZI_BOX_WIDTH + BOX_PAD)
    box_rows = draw_area_height / (HANZI_BOX_WIDTH + BOX_PAD)
    print "box rows: {} columns: {}".format(box_rows, box_columns)

    # Generate:
    for row in range(box_rows):
        for col in range(box_columns):
            # print "({}, {}) ".format(row, col),
            top = (s_top + (row * HANZI_BOX_WIDTH) + (row * BOX_PAD))
            left = (s_left + (col * HANZI_BOX_WIDTH) + (col * BOX_PAD))
            # print "row: {} col: {}, top: {}, left: {}".format(
            #     row, col, top, left)
            hanzi_box(draw, top, left, HANZI_BOX_WIDTH)

    # im.show()

    with open('static/output/hanzi_grid.png', 'wb') as fd:
        im.save(fd, "PNG")


if __name__ == "__main__":
    main()
