WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
BOARD_HEIGHT = 700
BOARD_WIDTH = 700
BOARD_DIMENSION = "16x16"
NUM_OF_BOARD_ITEMS = eval(BOARD_DIMENSION.replace("x", "*"))
BOARD_ROWS, BOARD_COLUMNS = map(int, BOARD_DIMENSION.split("x"))
ITEM_SPACING = 5
ITEM_SIZE = (BOARD_WIDTH // BOARD_ROWS) - ITEM_SPACING
