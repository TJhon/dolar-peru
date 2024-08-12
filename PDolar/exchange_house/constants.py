# left div
N_rows = 13
MIN_LEFT = 28
MIN_RIGHT = 2
COLUMNS_NAMES = [
    "actualizacion",
    "trash1",
    "compra",
    "variacion_compra",
    "venta",
    "variacion_venta",
    "img_url",
    "companny_url",
]

# Companny
range_left = list(range(MIN_LEFT, (MIN_LEFT + N_rows + 1)))
range_right = list(range(MIN_RIGHT, (MIN_RIGHT + N_rows + 1)))

PREV_XPATH = '//*[@id="__next"]/main/div[3]/'
