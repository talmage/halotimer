def circle(circleColor: number, milliseconds: number):
    for led3 in range(60):
        haloDisplay.set_zip_led_color(led3, circleColor)
        haloDisplay.show()
        basic.pause(milliseconds)
        haloDisplay.set_zip_led_color(led3, kitronik_halo_hd.colors(ZipLedColors.BLACK))
# Press button A to decrease the brightness of the LED

def on_button_pressed_a():
    global brightness
    if brightness > 0:
        brightness += -1
        haloDisplay.set_brightness(brightness)
input.on_button_pressed(Button.A, on_button_pressed_a)

# Press button B to increase the brightness of the LED

def on_button_pressed_ab():
    basic.show_string("Brightness:")
    basic.show_number(brightness)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Press button B to increase the brightness of the LED

def on_button_pressed_b():
    global brightness
    if brightness < 255:
        brightness += 1
        haloDisplay.set_brightness(brightness)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("Hey!")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# On the shake event, display the elapsed time in minutes.

def on_microbit_id_gesture_mes_device_shaken():
    basic.show_number(minutes)
control.on_event(EventBusSource.MICROBIT_ID_GESTURE,
    EventBusValue.MES_DEVICE_GESTURE_DEVICE_SHAKEN,
    on_microbit_id_gesture_mes_device_shaken)

minutes = 0
haloDisplay: kitronik_halo_hd.ZIPHaloHd = None
colors: List[number] = []
brightness = 0
led2 = 0
brightness = 128
colors.append(kitronik_halo_hd.colors(ZipLedColors.RED))
colors.append(kitronik_halo_hd.colors(ZipLedColors.ORANGE))
colors.append(kitronik_halo_hd.colors(ZipLedColors.YELLOW))
colors.append(kitronik_halo_hd.colors(ZipLedColors.GREEN))
colors.append(kitronik_halo_hd.colors(ZipLedColors.BLUE))
colors.append(kitronik_halo_hd.colors(ZipLedColors.INDIGO))
colors.append(kitronik_halo_hd.colors(ZipLedColors.VIOLET))
colors.append(kitronik_halo_hd.colors(ZipLedColors.PURPLE))
colors.append(kitronik_halo_hd.colors(ZipLedColors.WHITE))
haloDisplay = kitronik_halo_hd.create_zip_halo_display(60)
minutes = 0
haloDisplay.set_brightness(brightness)
haloDisplay.clear()
while True:
    for color in colors:
        circle(color, 1000)
        minutes += 1
        # Simulate the shake event so that the micro:bit displays the elapsed time in minutes.
        control.raise_event(EventBusSource.MICROBIT_ID_GESTURE,
            EventBusValue.MES_DEVICE_GESTURE_DEVICE_SHAKEN)