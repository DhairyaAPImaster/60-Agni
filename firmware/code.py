import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules import Module
from kmk.modules.layers import Layers
from kmk.modules.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

# ---- Matrix pins ----
keyboard.col_pins = (
    board.GP6, board.GP7, board.GP8, board.GP9, board.GP10,
    board.GP11, board.GP12, board.GP13, board.GP14, board.GP15,
    board.GP16, board.GP17, board.GP18, board.GP19,
)
keyboard.row_pins = (
    board.GP1, board.GP2, board.GP3, board.GP4, board.GP5,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

NUM_PIXELS = 61
rgb = RGB(
    pixel_pin=board.GP22,
    num_pixels=NUM_PIXELS,
    val_limit=100,
    hue_default=0,
    sat_default=100,
    val_default=80,
    animation_mode=AnimationModes.STATIC,
)
keyboard.modules.append(rgb)

try:
    import adafruit_ssd1306

    i2c = busio.I2C(scl=board.GP21, sda=board.GP20)
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

    class OLEDStatus(Module):
        """Minimal status display: shows current layer name."""

        def __init__(self, display):
            self.display = display
            self._last_layer = None

        def during_bootup(self, keyboard):
            self.display.fill(0)
            self.display.text('Agni V2', 0, 0, 1)
            self.display.text('Ready', 0, 12, 1)
            self.display.show()
            return keyboard

        def before_matrix_scan(self, keyboard):
            return keyboard

        def after_matrix_scan(self, keyboard):
            active = keyboard.active_layers[0] if keyboard.active_layers else 0
            if active != self._last_layer:
                self._last_layer = active
                self.display.fill(0)
                self.display.text('Agni V2', 0, 0, 1)
                label = 'Base' if active == 0 else 'Fn (L{})'.format(active)
                self.display.text(label, 0, 12, 1)
                self.display.show()
            return keyboard

        def process_key(self, keyboard, key, is_pressed, int_coord):
            return key

        def before_hid_send(self, keyboard):
            return keyboard

        def after_hid_send(self, keyboard):
            return keyboard

        def on_powersave_enable(self, keyboard):
            return keyboard

        def on_powersave_disable(self, keyboard):
            return keyboard

    keyboard.modules.append(OLEDStatus(oled))
except Exception as e:  # noqa: BLE001
    print('OLED init failed:', e)

_______ = KC.TRNS
XXXXXXX = KC.NO
keymap = [
    [
        # Row 0
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,  KC.N4,  KC.N5,  KC.N6,
        KC.N7,   KC.N8,   KC.N9,   KC.N0,  KC.MINS, KC.EQL, KC.BSPC,
        # Row 1
        KC.TAB,  KC.Q,    KC.W,    KC.E,   KC.R,   KC.T,   KC.Y,
        KC.U,    KC.I,    KC.O,    KC.P,   KC.LBRC, KC.RBRC, KC.BSLS,
        # Row 2
        KC.CAPS, KC.A,    KC.S,    KC.D,   KC.F,   KC.G,   KC.H,
        KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT, XXXXXXX,
        # Row 3
        KC.LSFT, KC.Z,    KC.X,    KC.C,   KC.V,   KC.B,   KC.N,
        KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, XXXXXXX, XXXXXXX,
        # Row 4
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.MO(1), KC.RALT, KC.RGUI,
        KC.RCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [
        # Layer 1: Fn layer - function keys, media, RGB controls
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,  KC.F4,  KC.F5,  KC.F6,
        KC.F7,   KC.F8,   KC.F9,   KC.F10, KC.F11, KC.F12, KC.DEL,
        _______, _______, _______, _______, _______, _______, _______,
        _______, _______, KC.PSCR, KC.HOME, KC.END, KC.INS, _______,
        _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, KC.PGUP, _______, KC.ENT, XXXXXXX,
        _______, _______, _______, _______, KC.LEFT, KC.DOWN, KC.UP,
        KC.RGHT, _______, _______, KC.PGDN, _______, XXXXXXX, XXXXXXX,
        _______, _______, _______, _______, _______, _______, _______,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    ],
]

keyboard.keymap = keymap

if __name__ == '__main__':
    keyboard.go()