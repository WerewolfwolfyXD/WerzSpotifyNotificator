import colorsys
import tkinter

from colorthief import ColorThief


def darken_color(rgb, factor):
    return tuple(max(0, int(c * (1 - factor))) for c in rgb)


def lighten_color(rgb, factor):
    return tuple(min(255, int(c + (255 - c) * factor)) for c in rgb)


def get_text_color(bg_color):
    r, g, b = bg_color
    h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
    if l > 0.5:  # 背景较亮
        return [(0, 0, 0), darken_color(bg_color, 0.8)]
    else:  # 背景较暗
        return [(255, 255, 255), lighten_color(bg_color, 0.8)]


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def get_theme_color():
    ct = ColorThief("cache.png")
    tc = ct.get_color(quality=1)
    txtc = get_text_color(tc)
    return {"ctheme": rgb_to_hex(tc), "ctext": rgb_to_hex(txtc[1]), "ctext_pure": rgb_to_hex(txtc[0])}
