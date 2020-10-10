def circle(circleColor: number, milliseconds: number):
    for led3 in range(60):
        haloDisplay.set_zip_led_color(led3, circleColor)
        haloDisplay.show()
        basic.pause(milliseconds)
        haloDisplay.set_zip_led_color(led3, kitronik_halo_hd.colors(ZipLedColors.BLACK))
haloDisplay: kitronik_halo_hd.ZIPHaloHd = None
colors: List[number] = []
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
led2 = 0
haloDisplay.set_brightness(111)
haloDisplay.clear()
while True:
    for color in colors:
        circle(color, 1000)